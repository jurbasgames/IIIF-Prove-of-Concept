from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from iiif_prezi3 import Manifest
from .models import Manifest, Canvas, AnnotationPage, Annotation, ImageResource
import os
from dotenv import load_dotenv
load_dotenv()
CANTALOUPE_URL = os.getenv("CANTALOUPE_URL")
