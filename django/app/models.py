from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Objeto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField()
    dimensoes = models.CharField(max_length=100)
    localizacao_atual = models.CharField(max_length=255, blank=True, null=True)
    imagem_arquivo = models.ImageField(
        upload_to='data/images', blank=True, null=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='objetos')

    class Meta:
        verbose_name_plural = "Objetos"

    def __str__(self):
        return self.titulo


class Colecao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    objetos = models.ManyToManyField(Objeto, related_name='colecoes')

    class Meta:
        verbose_name_plural = "Coleções"

    def __str__(self):
        return self.nome


class Visualizacao(models.Model):
    objeto = models.ForeignKey(
        Objeto, on_delete=models.CASCADE, related_name='visualizacoes')
    altura = models.IntegerField()
    largura = models.IntegerField()
    rotulo = models.CharField(max_length=255)
    formato = models.CharField(max_length=50)
    anotacoes = models.ManyToManyField(
        'Anotacao')

    class Meta:
        verbose_name_plural = "Visualizações"

    def __str__(self):
        return self.rotulo


class Anotacao(models.Model):
    texto = models.TextField()
    tipo = models.CharField(max_length=50)  # Comentário, Transcrição, Tradução
    altura = models.IntegerField()
    largura = models.IntegerField()
    dimensoes = models.CharField(max_length=100)
