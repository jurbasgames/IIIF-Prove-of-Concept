from django.shortcuts import get_object_or_404
from .models import Manifest as ManifestModel
from iiif_prezi3 import Manifest, config
import os
import urllib.parse

APP_HOST = os.getenv("APP_HOST", "http://localhost:8000")


def create_manifest(manifest_id):
    db_manifest = get_object_or_404(ManifestModel, pk=manifest_id)
    manifest_iiif = Manifest(
        id=f"{APP_HOST}/manifest/{db_manifest.pk}",
        type="Manifest",
        label={label.language: [label.value]
               for label in db_manifest.label.all()},
        summary={summary.language: [summary.value] for summary in db_manifest.summary.all(
        )} if db_manifest.summary.exists() else None
    )

    for db_canvas in db_manifest.items.all():
        canvas_iiif = manifest_iiif.make_canvas(
            id=f"{APP_HOST}/canvas/{db_canvas.pk}",
            height=db_canvas.height,
            width=db_canvas.width
        )

        for annotation_page in db_canvas.annotation_pages.all():
            anno_page_iiif = canvas_iiif.add_annotation_page(
                id=annotation_page.id)

            for annotation in annotation_page.items.all():
                image = annotation.body
                anno_iiif = anno_page_iiif.add_annotation(
                    id=f"{APP_HOST}/annotation/{annotation.pk}",
                    motivation=annotation.motivation,
                    on=canvas_iiif.id
                )
                anno_iiif.resource = anno_iiif.make_image(
                    id=image.id,
                    label={label.language: [label.value]
                           for label in image.label.all()},
                    format=image.format,
                    height=image.height,
                    width=image.width
                )

    return manifest_iiif.json(indent=2)
