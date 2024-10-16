from django.shortcuts import get_object_or_404
from digital_collection.settings import APP_HOST, IMAGE_SERVER
from .models import Manifest as ManifestModel, Canvas
from iiif_prezi3 import Manifest, Canvas, Annotation, AnnotationPage, ResourceItem


def create_manifest(object_id):
    db_manifest = get_object_or_404(ManifestModel, pk=object_id)
    manifest_iiif = Manifest(
        id=f"{APP_HOST}/manifest/{object_id}",
        type="Manifest",
        label={label.language: [label.value]
               for label in db_manifest.label.all()},
        summary={db_manifest.summary.language: [
            db_manifest.summary.value]} if db_manifest.summary else None
    )

    # Metadados
    metadata = []
    for data in db_manifest.metadata.all():
        md_item = {
            "label": {label.language: [label.value] for label in data.label.all()},
            "value": {value.language: [value.value] for value in data.value.all()}
        }
        metadata.append(md_item)
    manifest_iiif.metadata = metadata

    # Canvas
    canvases = []

    for canvas in db_manifest.items.all():
        canvas_iiif = Canvas(
            id=f"{APP_HOST}/manifest/{object_id}/canvas/{canvas.pk}",
            type="Canvas",
            height=canvas.height,
            width=canvas.width,
            label={label.language: [label.value]
                   for label in canvas.label.all()}
        )

        # Imagens
        painting_annotation_items = []
        for image in canvas.items.all():
            if image.external_url:
                image_url = image.external_url
            else:
                image_url = f"{IMAGE_SERVER}/iiif/3/{image.pk}.{image.format.lower()}/full/max/0/default.jpg"
            image_annotation = Annotation(
                id=f"{APP_HOST}/manifest/{object_id}/canvas/{canvas.pk}/annotation/{image.pk}",
                type="Annotation",
                motivation="painting",
                target=canvas_iiif.id,
                body=ResourceItem(
                    id=image_url,
                    format=f"image/{image.format.lower()}",
                    type="Image",
                    height=image.height,
                    width=image.width
                )
            )
            painting_annotation_items.append(image_annotation)

        if painting_annotation_items:
            painting_annotation_page = AnnotationPage(
                id=f"{APP_HOST}/manifest/{object_id}/canvas/{canvas.pk}/page/1",
                type="AnnotationPage",
                items=painting_annotation_items
            )
            canvas_iiif.items = [painting_annotation_page]

        # Anotações de texto
        non_painting_annotation_items = []
        for text_annotation in canvas.annotations.all():
            text_annotation_iiif = Annotation(
                id=f"{APP_HOST}/manifest/{object_id}/canvas/{canvas.pk}/textannotation/{text_annotation.pk}",
                type="Annotation",
                motivation=text_annotation.motivation,
                body={
                    "type": "TextualBody",
                    "value": text_annotation.text,
                    "language": text_annotation.language,
                    "format": "text/plain",
                },
                target=f"{APP_HOST}/manifest/{object_id}/canvas/{canvas.pk}/page/1#xywh={text_annotation.x},{text_annotation.y},{text_annotation.width},{text_annotation.height}"
            )
            non_painting_annotation_items.append(text_annotation_iiif)

        if non_painting_annotation_items:
            non_painting_annotation_page = AnnotationPage(
                id=f"{APP_HOST}/manifest/{object_id}/canvas/{canvas.pk}/textannotationpage",
                type="AnnotationPage",
                items=non_painting_annotation_items
            )
            canvas_iiif.items.append(non_painting_annotation_page)

        canvases.append(canvas_iiif)

    manifest_iiif.items = canvases

    return manifest_iiif.json(indent=2)
