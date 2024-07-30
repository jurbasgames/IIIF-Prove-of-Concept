# utils.py
from django.shortcuts import get_object_or_404
from .models import Manifest as ManifestModel, Canvas as CanvasModel
from iiif_prezi3 import Manifest, Canvas, Annotation, AnnotationPage, ResourceItem
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

    canvases = []

    for canvas in db_manifest.items.all():
        canvas_iiif = Canvas(
            id=f"{APP_HOST}/{object_id}/canvas/{canvas.pk}",
            type="Canvas",
            height=canvas.height,
            width=canvas.width,
            label={label.language: [label.value]
                   for label in canvas.label.all()}
        )

        painting_annotation_items = []
        for image in canvas.items.all():
            image_annotation = Annotation(
                id=f"{APP_HOST}/annotation/{image.pk}",
                type="Annotation",
                motivation="painting",
                target=canvas_iiif.id,
                body=ResourceItem(
                    id=f"{
                        IMAGE_SERVER}/{image.pk}.{image.format.lower()}/full/full/0/default.jpg",
                    format=f"image/{image.format.lower()}",
                    type="Image",
                    height=image.height,
                    width=image.width
                )
            )
            painting_annotation_items.append(image_annotation)

        if painting_annotation_items:
            painting_annotation_page = AnnotationPage(
                id=f"{APP_HOST}/{object_id}/page/{canvas.pk}/1",
                type="AnnotationPage",
                items=painting_annotation_items
            )
            canvas_iiif.items = [painting_annotation_page]

        non_painting_annotation_items = []
        for text_annotation in canvas.annotations.all():
            text_annotation_iiif = Annotation(
                id=f"{APP_HOST}/annotation/{text_annotation.pk}",
                type="Annotation",
                motivation=text_annotation.motivation,
                target=canvas_iiif.id,
                body=ResourceItem(
                    type="TextualBody",
                    value=text_annotation.text,
                    language=text_annotation.language
                )
            )
            non_painting_annotation_items.append(text_annotation_iiif)

        if non_painting_annotation_items:
            non_painting_annotation_page = AnnotationPage(
                id=f"{
                    APP_HOST}/{object_id}/canvas/{canvas.pk}/annotation-page/non-painting",
                type="AnnotationPage",
                items=non_painting_annotation_items
            )
            canvas_iiif.items.append(non_painting_annotation_page)

        canvases.append(canvas_iiif)

    manifest_iiif.items = canvases

    return manifest_iiif.json(indent=2)
