# utils.py
from django.shortcuts import get_object_or_404
from .models import Manifest as ManifestModel, Canvas as CanvasModel
from iiif_prezi3 import Manifest, Annotation
import os

APP_HOST = os.getenv("APP_HOST", "http://localhost:8000")
IMAGE_SERVER = os.getenv("IMAGE_SERVER", "http://localhost:3132/iiif")


def create_manifest(object_id):
    db_manifest = get_object_or_404(ManifestModel, pk=object_id)
    manifest_iiif = Manifest(
        id=f"{APP_HOST}/{object_id}/manifest",
        type="Manifest",
        label={label.language: [label.value]
               for label in db_manifest.label.all()},
        summary={db_manifest.summary.language: [
            db_manifest.summary.value]} if db_manifest.summary else None
    )

    for canvas in db_manifest.items.all():
        canvas_iiif = manifest_iiif.make_canvas(
            id=f"{APP_HOST}/{object_id}/canvas/{canvas.pk}",
            height=canvas.height,
            width=canvas.width
        )

        # Painting Annotations
        for image in canvas.items.all():
            image_annotation = Annotation(
                id=f"{APP_HOST}/annotation/{image.pk}",
                motivation="painting",
                target=canvas_iiif.id,
                body={
                    "id": f"{IMAGE_SERVER}/iiif/image/{image.pk}.{image.format}/full/full/0/default.jpg",
                    "type": "Image",
                    "format": f"image/{image.format.lower()}",
                    "height": image.height,
                    "width": image.width
                }
            )
            canvas_iiif.add_annotation(image_annotation)

        # Non-Painting Annotations
        for text_annotation in canvas.annotations.all():
            text_annotation_iiif = Annotation(
                id=f"{APP_HOST}/annotation/{text_annotation.pk}",
                motivation=text_annotation.motivation,
                target=canvas_iiif.id,
                body={
                    "type": "TextualBody",
                    "value": text_annotation.text,
                    "language": text_annotation.language
                }
            )
            canvas_iiif.add_annotation(text_annotation_iiif)

    return manifest_iiif.json(indent=2)
