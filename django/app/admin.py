from django.contrib import admin
from .models import Manifesto, Tela, PaginaAnotacao, Anotacao, Imagem

# Register your models here.

admin.site.register(Manifesto)
admin.site.register(Tela)
admin.site.register(PaginaAnotacao)
admin.site.register(Anotacao)
admin.site.register(Imagem)
