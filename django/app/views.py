from django.http import HttpResponse
from .utils import create_manifest


def manifest_view(request, manifest_id):
    manifest_json = create_manifest(manifest_id)
    return HttpResponse(manifest_json, content_type='application/json')
