from django.db import models
from django.utils import timezone


# Create your models here.

LISTA_CATEGORIA = (
    ("ANALISE", "Análise"), #armazenar no bd, aparecer_pro_usuario
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)

# Criar filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes') #imagem , usuario precisa arazenar a imagem, thum_filmes é a pasta aonde ficara armazenada as imagens
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA) # categoria de itens
    vizualizacoes = models.IntegerField(default=0) # para todos os filmes a vizualização se inicia em 0
    data_criacao = models.DateTimeField(default=timezone.now) # para cada filme, ele vai preencher automatio com a data e hora que for salvo


# Criar episodios


# Criar Usuario
