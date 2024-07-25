from django.db import models
import uuid


class Label(models.Model):
    language = models.CharField(max_length=10)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.language}: {self.value}"


class Manifest(models.Model):
    context = models.URLField(
        default="http://iiif.io/api/presentation/3/context.json")
    label = models.ManyToManyField(Label, related_name="manifest_labels")
    summary = models.ManyToManyField(Label, related_name="manifest_summaries")
    items = models.ManyToManyField('Canvas', related_name='manifests')

    def __str__(self):
        return f"{self.id} {self.label.first().value}"


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
        'AnnotationPage', related_name="canvas_items")
    painting_annotations = models.ManyToManyField(
        'Annotation', related_name="canvas_painting_annotations")

    class Meta:
        verbose_name_plural = "Canvases"

    def __str__(self):
        return self.id


class AnnotationPage(models.Model):
    items = models.ManyToManyField(
        'Annotation', related_name="annotation_page_items")

    def __str__(self):
        return self.id


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.ManyToManyField(Label, related_name="image_labels")
    format = models.CharField(max_length=50)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return self.id


class Annotation(models.Model):
    target = models.ForeignKey(
        'Canvas', on_delete=models.CASCADE, related_name='target_annotations')
    body = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='annotations_as_body')
    motivation = models.CharField(max_length=255)

    def __str__(self):
        return self.id
