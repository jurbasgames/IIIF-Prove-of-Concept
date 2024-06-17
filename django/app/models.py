from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Item(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField()
    dimensoes = models.CharField(max_length=100)
    localizacao_atual = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=50)  # pintura, manuscrito, fotografia
    imagem_arquivo = models.ImageField(
        upload_to='imagens/', blank=True, null=True)  # Trocar para pasta do Cantaloupe
    categorias = models.ManyToManyField(Categoria, related_name='itens')

    class Meta:
        verbose_name_plural = "Itens"

    def __str__(self):
        return self.titulo


class Colecao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    itens = models.ManyToManyField(Item, related_name='colecoes')

    class Meta:
        verbose_name_plural = "Coleções"

    def __str__(self):
        return self.nome
