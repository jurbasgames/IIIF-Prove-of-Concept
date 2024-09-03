from django.core.management.base import BaseCommand
from app.models import Manifest, Metadata, Label


class Command(BaseCommand):
    help = 'Popula um manifesto específico com metadados automatizados'

    def handle(self, *args, **kwargs):
        manifesto_id = 3
        manifesto = Manifest.objects.get(id=manifesto_id)

        # Lista de metadados para adicionar
        metadados = {
            "dc:publisher": "FGV CPDOC",
            "dc:title": "Alto comando e outros membros da Coluna Prestes",
            "dc:date": "1925-10",
            "dc:format_1": "filme p&b 170/1/8-8A",
            "dc:subject": "Coluna Prestes; Tenentismo; História do Brasil; Primeira República; Revolta; Guerra em movimento",
            "dc:description": "Esq./dir.: (sentados)Djalma Dutra, Siqueira Campos, Luís Carlos Prestes, Miguel Costa, Juarez Távora, João Alberto e Cordeiro de Farias; (em pé)Pinheiro Machado, Atanagildo França, Emídio da Costa, João Pedro, Paulo kruger da Cunha Cruz, Ari Salgado freire, Nélson Machado, Manuel Lima Nascimento, Sadi Vale Machado, Trifino Correia e Ítalo Landucci",
            "dc:identifier": "JT foto 0571",
            "dc:relation": "Juarez Távora",
            "dc:type": "Fotografias",
            "dc:coverage": "Porto Nacional, Goiás, Brasil"
        }

        for chave, valor in metadados.items():
            # Cria labels para chave e valor
            chave_label, created = Label.objects.get_or_create(
                language='pt', value=chave)
            valor_label, created = Label.objects.get_or_create(
                language='pt', value=valor)

            # Cria o metadata e adiciona os labels
            metadata = Metadata.objects.create(manifest=manifesto)
            metadata.label.add(chave_label)
            metadata.value.add(valor_label)

        self.stdout.write(self.style.SUCCESS(
            'Metadados criados com sucesso para o manifesto ID 3.'))
