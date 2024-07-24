from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Objeto, Visualizacao


@receiver(post_save, sender=Objeto)
def criar_canvas_padrao(sender, instance, created, **kwargs):
    if created:
        Visualizacao.objects.create(
            objeto=instance,
            altura=1800,  # Verificar esses valores
            largura=1200,
            rotulo="Default"
        )
