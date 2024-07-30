# utils.py
from django.shortcuts import get_object_or_404
from .models import Manifest as ManifestModel, AnnotationPage as AnnotationPageModel
from iiif_prezi3 import Manifest
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
        summary={db_manifest.summary.language: [db_manifest.summary.value]
                 } if db_manifest.summary else None
    )

    for canva in db_manifest.items.all():
        canvas_iiif = manifest_iiif.make_canvas(
            id=f"{APP_HOST}/{object_id}/canvas/{canva.pk}",
            height=canva.height,
            width=canva.width
        )

        # Painting Annotations
        if canva.items:
            annotation_page = canva.items
            for image in annotation_page.images.all():
                image_annotation = canvas_iiif.make_annotation(
                    motivation="painting",
                    target=canvas_iiif.id,
                    body={
                        "id": f"{IMAGE_SERVER}/iiif/image/{image.pk}.{image.format}/full/full/0/default.jpg",
                        "type": "Image",
                        "format": image.format,
                        "height": image.height,
                        "width": image.width
                    }
                )
                canvas_iiif.add_annotation(image_annotation)

        # Non-Painting Annotations
        if canva.annotations:
            annotation_page = canva.annotations
            for text_annotation in annotation_page.text_annotations.all():
                text_annotation_iiif = canvas_iiif.make_annotation(
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
