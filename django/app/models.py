from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image as PilImage
from django.core.files.base import ContentFile
import io


class Label(models.Model):
    language = models.CharField(max_length=10, db_index=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.language}: {self.value}"


class Manifest(models.Model):
    context = models.URLField(
        default="http://iiif.io/api/presentation/3/context.json")
    label = models.ManyToManyField(Label, related_name="manifest_labels")
    summary = models.ManyToManyField(Label, related_name="manifest_summaries")
    items = models.ManyToManyField(
        'Canvas', related_name='manifests', blank=True)

    def __str__(self):
        label = self.label.first()
        return f"{self.id} {label.value if label else 'No Label'}"


class Metadata(models.Model):
    manifest = models.ForeignKey(
        Manifest, on_delete=models.CASCADE, related_name='metadata')
    label = models.ManyToManyField(Label, related_name="metadata_labels")
    value = models.ManyToManyField(Label, related_name="metadata_values")

    def __str__(self):
        return f"Metadata for {self.manifest.id}"


class Canvas(models.Model):
    label = models.ManyToManyField(Label, related_name="canvas_labels")
    height = models.IntegerField()
    width = models.IntegerField()
    annotation_pages = models.ManyToManyField(
        'AnnotationPage', related_name="canvas_items", blank=True)
    images = models.ManyToManyField(
        'Image',
        related_name='canvas_images',
        blank=True
    )

    class Meta:
        verbose_name_plural = "Canvases"

    def __str__(self):
        label = self.label.first()
        return f"{self.id} {label.value if label else 'No Label'}"


class AnnotationPage(models.Model):
    items = models.ManyToManyField(
        'Annotation', related_name="annotation_page_items")

    def __str__(self):
        return str(self.id)


class Annotation(models.Model):
    target = models.ForeignKey(
        Canvas, on_delete=models.CASCADE, related_name='annotations')
    label = models.ManyToManyField(Label, related_name="annotation_labels")
    motivation = models.CharField(max_length=255, default='commenting', choices=[(
        'comment', 'Comentário'), ('highlight', 'Destaque'), ('scanning', 'Digitalização')])
    body_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Annotation {self.id} on {self.target.id}"


class Image(models.Model):
    canvases = models.ManyToManyField(
        Canvas,
        blank=True
    )
    format = models.CharField(
        max_length=50, db_index=True, blank=True)
    height = models.IntegerField(
        validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    width = models.IntegerField(
        validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    file = models.FileField(upload_to='data/images/', null=True, blank=True)

    def __str__(self):
        canvas_ids = ", ".join(str(canvas.id)
                               for canvas in self.canvases.all())
        return f"Image {self.id} on Canvas {canvas_ids if canvas_ids else 'No Canvas'}"

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Image, self).save(*args, **kwargs)

        if self.file:
            img = PilImage.open(self.file)
            self.width, self.height = img.size
            if not self.format:
                self.format = img.format

            new_filename = f"{self.id}.{self.format.lower()}"

            buffer = io.BytesIO()
            img.save(buffer, format=self.format)
            file_content = ContentFile(buffer.getvalue())

            self.file.delete(save=False)
            self.file.save(new_filename, file_content, save=False)

            buffer.close()

        super(Image, self).save(*args, **kwargs)
