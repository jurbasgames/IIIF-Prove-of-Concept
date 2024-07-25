from django.contrib import admin
from .models import Manifest, Canvas, AnnotationPage, Image, Label, Metadata, Annotation

# Register your models here.

admin.site.register(Manifest)
admin.site.register(Canvas)
admin.site.register(AnnotationPage)
admin.site.register(Image)
admin.site.register(Label)
admin.site.register(Metadata)
admin.site.register(Annotation)
