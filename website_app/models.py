from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
# from storages.backends.ftp import FTPStorage
# SERVIDOR_FTP_WEB = FTPStorage()
from .models_includes import *

class Jogador(models.Model):
    nome = models.CharField('Nome',max_length=255,null=True,blank=True)
    idade = models.IntegerField('Idade',default=10,null=True,blank=True)
    login = models.CharField('Login',max_length=255,null=True,blank=True)
    password = models.CharField('Senha',max_length=255,null=True,blank=True)
    genero = models.CharField('Genero',choices=GENERO,max_length=10,default='M',null=True,blank=True)
    nivel_de_autismo = models.CharField('Nível de Autismo',choices=NIVEL_DE_AUTISMO,max_length=50,null=True,blank=True)
    definicao_a_1 = models.CharField('Definiçao A-1',choices=DEFINITION_A_1,max_length=20,null=True,blank=True)
    definicao_a_2 = models.CharField('Definiçao A-2',choices=DEFINITION_A_2,max_length=20,null=True,blank=True)
    definicao_a_3 = models.CharField('Definiçao A-3',choices=DEFINITION_A_3,max_length=20,null=True,blank=True)
    definicao_b_1 = models.CharField('Definiçao B-1',choices=DEFINITION_B_1,max_length=20,null=True,blank=True)
    definicao_b_2 = models.CharField('Definiçao B-2',choices=DEFINITION_B_2,max_length=20,null=True,blank=True)
    definicao_b_3 = models.CharField('Definiçao B-3',choices=DEFINITION_B_3,max_length=20,null=True,blank=True)
    definicao_b_4 = models.CharField('Definiçao B-4',choices=DEFINITION_B_4,max_length=20,null=True,blank=True)
    definicao_c = models.CharField('Definiçao C',choices=DEFINITION_C,max_length=20,null=True,blank=True)
    definicao_d = models.CharField('Definiçao D',choices=DEFINITION_D,max_length=20,null=True,blank=True)
    definicao_e = models.CharField('Definiçao E',choices=DEFINITION_E,max_length=20,null=True,blank=True)
    def __str__(self):
        return str(self.nome)+" "+str(self.idade)+" Anos"

    def get_absolute_url(self):
        return reverse('website_app:Jogadores')

class Personagem(models.Model):
    descricao = models.CharField("Descrição",max_length=100)
    prefab = models.CharField(max_length=50)
    tamanho = models.CharField("Tamanho(Usar virgula): ",max_length=10,default="1,0")
    def __str__(self):
        return str(self.descricao)

class Objeto_er(models.Model):
    personagem = models.ForeignKey(Personagem, on_delete=models.PROTECT,null=True,blank=True)
    titulo = models.CharField('Titulo do objeto de aprendizagem',max_length=255,null=True,blank=True)
    sub_titulo = models.CharField('Sub titulo',max_length=255,null=True,blank=True)
    descricao = models.CharField('Descrição',max_length=255,null=True,blank=True)
    area_de_conhecimento = models.CharField('Área de Conhecimento',choices=AREA_DE_CONHECIMENTO,max_length=50,null=True,blank=True)
    dificuldade = models.CharField('Nível de dificuldade',choices=DIFICULDADE,max_length=20,null=True,blank=True)
    tipo_de_arquivo = models.CharField('Tipo de arquivo',max_length=10,choices=TIPO_DE_ARQUIVO,null=True,blank=True)
    #Text
    autor = models.ForeignKey(User, on_delete=models.PROTECT,null=True,blank=True)
    texto = models.CharField('Texto',max_length=255,null=True,blank=True)
    idioma = models.CharField('Idioma',max_length=10,choices=IDIOMA,null=True,blank=True)
    #Imagem
    #arquivo = models.FileField(upload_to='arquivos/objeto_er/',storage=SERVIDOR_FTP_WEB)
    arquivo_1 = models.FileField('Arquivo Principal',upload_to='arquivos/objeto_er/',null=True,blank=True)
    arquivo_2 = models.FileField('Arquivo Secundário:',upload_to='arquivos/objeto_er/',null=True,blank=True)
    #Audio, Video
    duracao = models.IntegerField("Duração em Minutos",default=0,null=True,blank=True)
    def __str__(self):
        return str(self.personagem)+" - "+str(self.titulo)

    def get_absolute_url(self):
        return reverse('website_app:Objeto_ers')

class Objeto_er_map(models.Model):
    latitude = models.CharField('Latitude',max_length=255,null=True,blank=True)
    longitude = models.CharField('Longitude',max_length=255,null=True,blank=True)
    objeto_er = models.ForeignKey(Objeto_er, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.objeto_er)

    def get_absolute_url(self):
        return reverse('website_app:Objeto_er_maps')

class Captura(models.Model):
    latitude = models.CharField(max_length=255,null=True,blank=True)
    longitude = models.CharField(max_length=255,null=True,blank=True)
    objeto_er = models.ForeignKey(Objeto_er, on_delete=models.CASCADE)
    data = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.objeto_er)

    def get_absolute_url(self):
        return reverse('website_app:index')
