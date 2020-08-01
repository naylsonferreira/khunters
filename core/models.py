from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from storages.backends.ftp import FTPStorage
import os
SERVIDOR_FTP_WEB = FTPStorage()

GENERO = (('M','Masculino'),('F','Feminino'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField("Foto do perfil",upload_to='profiles/',storage=SERVIDOR_FTP_WEB,null=True,blank=True)
    sobre = models.TextField("Escreva algo sobre você",null=True,blank=True)
    whatsapp = models.CharField(max_length=50,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    idade = models.IntegerField('Idade',default=18,null=True,blank=True)
    genero = models.CharField('Genero',choices=GENERO,max_length=10,default='M',null=True,blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('website:index')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()