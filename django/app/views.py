from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from iiif_prezi3 import Manifest
from .models import Objeto, Visualizacao
import os
from dotenv import load_dotenv
load_dotenv()
CANTALOUPE_URL = os.getenv("CANTALOUPE_URL")


def iiif_manifest(request, image_id):
    # Carrega configurações de idioma
    from iiif_prezi3 import config
    config.configs['helpers.auto_fields.AutoLang'].auto_lang = "pt"

    # Busca o objeto da base de dados
    objeto = get_object_or_404(Objeto, id=image_id)

    # Cria o manifesto com base no Objeto recuperado
    manifest = Manifest(
        id=f"https://{CANTALOUPE_URL}/{image_id}",
        label=objeto.titulo,
        description=objeto.descricao if hasattr(
            objeto, 'descricao') else "Sem descrição disponível."
    )

    # Adiciona canvas ao manifesto para cada visualização associada ao objeto
    for visualizacao in objeto.visualizacoes.all():
        canvas_id = f"https://{CANTALOUPE_URL}/canvas/{visualizacao.id}"
        image_url = visualizacao.imagem_url

        # Cria um Canvas no Manifesto
        canvas = manifest.make_canvas(
            id=canvas_id,
            height=visualizacao.altura,
            width=visualizacao.largura
        )

        # Adiciona uma página de anotação ao Canvas
        canvas.add_image(
            image_url=image_url,
            anno_page_id=f"{canvas_id}/page/1",
            anno_id=f"{canvas_id}/annotation/1",
            format="image/jpeg",  # Presumindo JPEG, ajuste conforme necessário
            height=visualizacao.altura,
            width=visualizacao.largura
        )

    # Retorna o manifesto serializado em JSON
    return HttpResponse(manifest.json(indent=2), content_type="application/json")
