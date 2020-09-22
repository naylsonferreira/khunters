from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers, viewsets
from django.http import JsonResponse,HttpResponse
from django.core.validators import validate_email
from .serializers import *
import json
import time
from random import randrange
from math import sqrt
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import distance

class JogadorList(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class Objeto_erList(viewsets.ModelViewSet):
    queryset = Objeto_er.objects.all()
    serializer_class = Objeto_erSerializer

class Objeto_er_mapList(viewsets.ModelViewSet):
    queryset = Objeto_er_map.objects.all()
    serializer_class = Objeto_er_mapSerializer

class CapturaList(viewsets.ModelViewSet):
    queryset = Captura.objects.all()
    serializer_class = CapturaSerializer

def criar_automaticamente(latitude,longitude):
    lista = Objeto_er.objects.all()
    for obj_er in lista:
        latitude = latitude  - (0.0001 * randrange(9) )
        longitude = longitude  - (0.0001 * randrange(9) )
        Objeto_er_map.objects.get_or_create(objeto_er_id=obj_er.id,latitude = latitude,longitude = longitude)
    

@api_view(['GET'])
def personagens_proximos(request):
    try:
        latitude = float(request.headers["Latitude"].replace(",","."))
        longitude = float(request.headers["Longitude"].replace(",","."))
        
        try:
            animacao = request.headers["Animacao"]
        except:
            animacao = "default"
        
        try:
            avatar = request.headers["Avatar"]
        except:
            avatar = "default"

        localizacao_player = (latitude,longitude)
    except:
        erro = "Enviar a localizacao latitude e longitude via cabeçalho"
        return JsonResponse(erro,status=400,safe=False)
    personagens = []
    jogadores = []
    mochila = []
    
    if request.auth:
        user = Token.objects.get(key=request.auth).user
    else:
        user = request.user
    
    jogador = Jogador.objects.get(user=user)

    jogador.latitude = latitude
    jogador.longitude = longitude
    jogador.avatar = avatar
    jogador.animacao = animacao
    jogador.online = True
    jogador.save()

    for obj_er_map in Objeto_er_map.objects.all():
        try:
            localizacao_personagem = (obj_er_map.latitude,obj_er_map.longitude)
            distancia = 1000 * distance(localizacao_player, localizacao_personagem).km
            if distancia <= 50: # Mostrar personagens com 500 metros ou menos do jogador
                j = Objeto_er_mapSerializer(obj_er_map)
                personagens.append(j.data)
        except:
            pass
    for jogador_map in Jogador.objects.filter(online=True).exclude(pk=jogador.pk):
        try:
            localizacao_jogador = (jogador_map.latitude,jogador_map.longitude)
            distancia = 1000 * distance(localizacao_player, localizacao_jogador).km
            if distancia <= 500: # Mostrar personagens com 500 metros ou menos do jogador
                j = JogadorSerializer(jogador_map)
                jogadores.append(j.data)
        except:
            pass

    if len(personagens) == 0 : criar_automaticamente(latitude,longitude)
    for item in Mochila.objects.all().filter(user=user):
        mochila.append({"prefab":item.personagem.prefab, "quantidade":item.quantidade})
    resultado = {
        "personagens":personagens,
        "jogadores":jogadores,
        "mochila":mochila
    }
    
    return JsonResponse(resultado,safe=False)

@api_view(['GET'])
def me(request):
    if request.auth:
        user = Token.objects.get(key=request.auth).user
    else:
        user = request.user
    
    try:
        jogador = user.jogador
    except:
        jogador = Jogador(user=user)
        jogador.save()

    return JsonResponse(JogadorSerializer(jogador,many=False).data,safe=False)

@api_view(['GET','POST'])
@parser_classes([JSONParser,MultiPartParser,FormParser])
def mochila(request, format=None):
    if request.auth:
        user = Token.objects.get(key=request.auth).user
    else:
        user = request.user

    if request.method == 'POST':
        try:
            try:
                objeto_er_map = request.data["objeto_er_map"]
                objeto_er_map = Objeto_er_map.objects.get(id=objeto_er_map)
                personagem = objeto_er_map.objeto_er.personagem
                objeto_er_map.delete()
            except:
                personagem = request.data["personagem"]
                personagem = Personagem.objects.get(id=personagem)
            quantidade = request.data["quantidade"]
            Mochila.objects.get_or_create(user=user,personagem=personagem)
            mochila = Mochila.objects.get(user=user,personagem=personagem)
            mochila.quantidade += int(quantidade)
            if mochila.quantidade < 0: mochila.quantidade = 0
            mochila.save()
        except:
            error = {"personagem": "Obrigatorio","quantidade": "Obrigatorio"}
            return JsonResponse({"error":error},status=400,safe=False)
    mochila = MochilaSerializer(Mochila.objects.all().filter(user=user), many=True).data
    return JsonResponse(mochila,safe=False)

def job_check_online_users(request):
    time.sleep(10)
    Jogador.objects.all().update(online=False)
    return HttpResponse("Ok")