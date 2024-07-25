from django.http import JsonResponse, HttpResponse
from .utils import create_manifest


def manifest_view(request, image_id):
    manifest_json = create_manifest(image_id)
    return HttpResponse(manifest_json, content_type='application/json')
