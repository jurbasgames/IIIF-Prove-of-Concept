from django.contrib import admin
from .models import Manifest, Canvas, Image, Label, Metadata, TextAnnotation

# Register your models here.


@admin.register(Manifest)
class ManifestAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_label')

    def get_label(self, obj):
        return obj.label.first().value if obj.label.exists() else 'No Label'
    get_label.short_description = 'Label'


@admin.register(Canvas)
class CanvasAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_label', 'height', 'width')

    def get_label(self, obj):
        return obj.label.first().value if obj.label.exists() else 'No Label'
    get_label.short_description = 'Label'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'format', 'height', 'width')


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('language', 'value')


@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    list_display = ('manifest',)


@admin.register(TextAnnotation)
class TextAnnotationAdmin(admin.ModelAdmin):
    list_display = ('motivation', 'text', 'language')
