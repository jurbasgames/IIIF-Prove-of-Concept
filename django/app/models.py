from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image as PilImage
from django.core.files.base import ContentFile
import io


class Label(models.Model):
    language = models.CharField(
        max_length=10, db_index=True, default=None, blank=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        label = self.label.first()
        return f"{self.id} {label.value if label else 'No Label'}"


class Image(models.Model):
    format = models.CharField(
        max_length=50, db_index=True, blank=True)
    height = models.IntegerField(
        validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    width = models.IntegerField(
        validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    file = models.FileField(upload_to='data/images/')
    annotation_page = models.ForeignKey(
        'AnnotationPage', on_delete=models.CASCADE, related_name='images', blank=True, null=True)

    def __str__(self):
        return f"Image {self.id} on AnnotationPage {self.annotation_page.id}"

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


class AnnotationPage(models.Model):

    def __str__(self):
        return f"AnnotationPage {self.id}"


class TextAnnotation(models.Model):
    annotation_page = models.ForeignKey(
        AnnotationPage, on_delete=models.CASCADE, related_name='text_annotations')
    label = models.ManyToManyField(Label, related_name="annotation_labels")
    motivation = models.CharField(max_length=255, default='tag', choices=[
        ('comment', 'Comentário'), ('tag', 'Tag'), ('scanning', 'Digitalização'), ('transcribing', 'Transcrição')])
    text = models.TextField()
    language = models.CharField(max_length=10, db_index=True)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"Annotation {self.id} on {self.target.id}"


class Canvas(models.Model):
    label = models.ManyToManyField(Label, related_name="canvas_labels")
    height = models.IntegerField()
    width = models.IntegerField()
    # AnnotationPage for Painting Annotations
    items = models.ForeignKey(AnnotationPage, on_delete=models.CASCADE,
                              related_name='canvas_items', blank=True, null=True)

    # AnnotationPage for Non-Painting Annotations
    annotations = models.ForeignKey(
        AnnotationPage, on_delete=models.CASCADE, related_name='canvas_annotation_page', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Canvases"

    def __str__(self):
        label = self.label.first()
        return f"{self.id} {label.value if label else 'No Label'}"


class Manifest(models.Model):
    context = models.URLField(
        default="http://iiif.io/api/presentation/3/context.json")
    label = models.ManyToManyField(Label, related_name="manifest_labels")
    summary = models.ForeignKey(
        Label, on_delete=models.CASCADE, related_name="manifest_summaries", blank=True, null=True)
    items = models.ManyToManyField(
        Canvas, related_name='manifests', blank=True)


class Metadata(models.Model):
    manifest = models.ForeignKey(
        Manifest, on_delete=models.CASCADE, related_name='metadata')
    label = models.ManyToManyField(Label, related_name="metadata_labels")
    value = models.ManyToManyField(Label, related_name="metadata_values")

    def __str__(self):
        return f"Metadata for {self.manifest.id}"
