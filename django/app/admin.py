from django.contrib import admin
from .models import Objeto, Categoria, Colecao, Visualizacao, Anotacao

# Register your models here.

admin.site.register(Objeto)
admin.site.register(Categoria)
admin.site.register(Colecao)
admin.site.register(Visualizacao)
admin.site.register(Anotacao)
