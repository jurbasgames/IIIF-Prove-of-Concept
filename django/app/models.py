from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image as PilImage
from django.core.files.base import ContentFile
import io
from django.forms import ValidationError
import requests


class Label(models.Model):
    language = models.CharField(
        max_length=10, db_index=True, default="None", blank=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.language}: {self.value}"


class Image(models.Model):
    format = models.CharField(max_length=50, db_index=True, blank=True)
    height = models.IntegerField(
        validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    width = models.IntegerField(
        validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    file = models.FileField(blank=True, null=True)
    external_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

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

        elif self.external_url:
            splitted_url = self.external_url.split("/")
            format = splitted_url[-1].split(".")[1]
            iiif_info_url = "/".join(splitted_url[:-4]) + "/info.json"
            try:
                response = requests.get(iiif_info_url)
                iiif_info = response.json()
                self.width = iiif_info['width']
                print(iiif_info['width'])
                self.height = iiif_info['height']
                print(iiif_info['height'])
                self.format = format
                print(iiif_info['@id'].split('.')[-1].upper())
            except Exception as e:
                raise ValueError(
                    f"Erro ao obter metadados da imagem IIIF: {e}")

        super().save(*args, **kwargs)

    def clean(self):
        if not self.file and not self.external_url:
            raise ValidationError(
                "Deve fornecer uma imagem local ou uma URL IIIF.")
        if self.file and self.external_url:
            raise ValidationError(
                "Deve fornecer apenas uma imagem local ou uma URL IIIF, não ambas.")


class TextAnnotation(models.Model):
    motivation = models.CharField(max_length=255, default='comment', choices=[
        ('comment', 'Comentário'), ('tag', 'Tag'), ('scanning', 'Digitalização'), ('transcribing', 'Transcrição')])
    text = models.TextField()
    language = models.CharField(max_length=10, db_index=True)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    canvas = models.ForeignKey('Canvas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.motivation}: {self.text[:30]}"


class Canvas(models.Model):
    label = models.ManyToManyField(Label, related_name="canvas_labels")
    height = models.IntegerField()
    width = models.IntegerField()
    items = models.ManyToManyField(Image, related_name='canvases', blank=True)
    annotations = models.ManyToManyField(
        TextAnnotation, related_name='canvases', blank=True)

    class Meta:
        verbose_name_plural = "Canvases"

    def __str__(self):
        label = self.label.first()
        return f"Canvas {self.id} ({label.value if label else 'No Label'})"


class Manifest(models.Model):
    context = models.URLField(
        default="http://iiif.io/api/presentation/3/context.json")
    label = models.ManyToManyField(Label, related_name="manifest_labels")
    summary = models.ForeignKey(Label, on_delete=models.CASCADE,
                                related_name="manifest_summaries", blank=True, null=True)
    items = models.ManyToManyField(
        Canvas, related_name='manifests', blank=True)

    def __str__(self):
        label = self.label.first()
        return f"Manifest {self.id} ({label.value if label else 'No Label'})"


class Metadata(models.Model):
    manifest = models.ForeignKey(
        Manifest, on_delete=models.CASCADE, related_name='metadata')
    label = models.ManyToManyField(Label, related_name="metadata_labels")
    value = models.ManyToManyField(Label, related_name="metadata_values")

    def __str__(self):
        return f"Metadata for Manifest {self.manifest.id}"
