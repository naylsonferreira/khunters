from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from storages.backends.ftp import FTPStorage
import os
SERVIDOR_FTP_WEB = FTPStorage()

GENERO = (('M','Masculino'),('F','Feminino'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True,null=True)
    nome = models.CharField('Nome completo',max_length=50,null=True,blank=True)
    apelido = models.CharField('Como gostaria de ser chamado?',max_length=50,null=True,blank=True)
    foto = models.ImageField("Foto do perfil",upload_to='profiles/',storage=SERVIDOR_FTP_WEB,null=True,blank=True)
    sobre = models.TextField("Escreva algo sobre você",null=True,blank=True)
    whatsapp = models.CharField(max_length=50,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    idade = models.IntegerField('Idade',default=18,null=True,blank=True)
    genero = models.CharField('Gênero',choices=GENERO,max_length=10,default='M',null=True,blank=True)

    def __str__(self):
        return str(self.email)

    def get_absolute_url(self):
        return ('/profile')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,email=instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, **kwargs):
    user = instance.user.pk
    user = User.objects.get(pk=user)
    user.username = instance.email
    user.email = instance.email
    user.save()

    