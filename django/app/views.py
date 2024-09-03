from django.http import HttpResponse
from django.shortcuts import render
from app.models import Manifest
from digital_collection.settings import APP_HOST
from .utils import create_manifest


def manifest_view(request, manifest_id):
    manifest_json = create_manifest(manifest_id)
    return HttpResponse(manifest_json, content_type='application/json')


def mirador_view(request):
    manifestos = Manifest.objects.all()

    manifestos_dict = {}
    for manifest in manifestos:
        manifest_url = f'{APP_HOST}/manifest/{manifest.id}/'
        manifestos_dict[manifest_url] = {"provider": ""}

    print("Manifestos Dicionário:", manifestos_dict)

    context = {
        'manifestos_dict': manifestos_dict,
        'primeiro_manifesto': list(manifestos_dict.keys())[0] if manifestos_dict else None,
    }

    return render(request, 'mirador.html', context)
