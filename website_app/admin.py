from django.contrib import admin
from .models import Jogador, Mochila, Objeto_er_map, Objeto_er, Captura, Personagem

admin.site.register({Jogador, Mochila, Objeto_er,
                     Captura, Objeto_er_map, Personagem})
