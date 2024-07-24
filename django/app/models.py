from django.db import models
from PIL import Image


class Manifesto(models.Model):
    tipo = models.CharField(max_length=50, default='Manifest')
    rotulo = models.JSONField()  # Campos models.JSONField podem ser multi-idiomas
    resumo = models.JSONField(blank=True, null=True)
    metadados = models.JSONField(blank=True, null=True,
                                 help_text="Metadados adicionais em formato JSON")

    # Relacionamentos
    itens = models.ManyToManyField(
        'Tela', related_name='manifestos', blank=True)

    def __str__(self):
        return self.rotulo.get('pt', 'Sem rótulo')


class Tela(models.Model):
    rotulo = models.JSONField()
    largura = models.IntegerField()
    altura = models.IntegerField()

    class Meta:
        verbose_name = 'Tela'
        verbose_name_plural = 'Telas'

    def __str__(self):
        return self.rotulo.get('pt', 'Sem rótulo')


class PaginaAnotacao(models.Model):
    tela = models.ForeignKey(
        Tela, on_delete=models.CASCADE, related_name='paginas_anotacoes')

    def __str__(self):
        return f'Página de Anotação {self.id}'


class Anotacao(models.Model):
    texto = models.TextField(blank=True, null=True)
    rotulo = models.JSONField(blank=True, null=True)
    pagina_anotacao = models.ForeignKey(
        PaginaAnotacao, on_delete=models.CASCADE, related_name='anotacoes')
    motivo = models.CharField(max_length=50, choices=[
        ('comment', 'Comentário'),
        ('describing', 'Descrição'),
        ('highlighting', 'Destaque'),
        ('scanning', 'Digitalização')
    ], default='comment')
    x = models.IntegerField(
        help_text="Coordenada X do canto superior esquerdo")
    y = models.IntegerField(
        help_text="Coordenada Y do canto superior esquerdo")
    largura = models.IntegerField(help_text="Largura da área anotada")
    altura = models.IntegerField(help_text="Altura da área anotada")
    # Relacionamentos
    imagem = models.ForeignKey(
        'Imagem', on_delete=models.CASCADE)

    def __str__(self):
        return f'Anotação {self.id} - {self.motivo}'

    def get_xywh(self):
        """Retorna a string xywh."""
        return f"{self.x},{self.y},{self.largura},{self.altura}"


class Imagem(models.Model):
    tipo = models.CharField(max_length=50, choices=[
        ('fotografia', 'Fotografia'),
        ('pintura', 'Pintura'),
        ('manuscrito', 'Manuscrito'),
        ('outro', 'Outro')
    ], default='fotografia')
    formato = models.CharField(max_length=50, choices=[
        ('jpeg', 'JPEG'),
        ('tiff', 'TIFF'),
        ('png', 'PNG')
    ], default='tiff')
    arquivo_imagem = models.ImageField(upload_to='data/images')
    altura = models.IntegerField(blank=True, null=True)
    largura = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Imagem {self.id} - {self.formato}'

    def save(self, *args, **kwargs):
        if self.arquivo_imagem and not self.altura:
            img = Image.open(self.arquivo_imagem)
            self.largura, self.altura = img.size
        super().save(*args, **kwargs)
