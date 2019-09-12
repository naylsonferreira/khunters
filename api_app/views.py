from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers, viewsets
from django.http import JsonResponse,HttpResponse
from .serializers import *
import json
from math import sqrt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import distance

#Acesso ao usuario via Token
#request.user will be a Django User instance.
#request.auth will be a rest_framework.authtoken.models.Token instance.

# ViewSets define the view behavior.
# @permission_classes((IsAuthenticatedOrReadOnly,))
# class ProdutoList(viewsets.ModelViewSet):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer
#     def get_queryset(self):
#         return self.queryset.filter(em_estoque=True)

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

@csrf_exempt
def personagens_proximos(request):
    try:
        dados = json.loads(request.body)
        latitude = float(dados["localizacao"]["latitude"])
        longitude = float(dados["localizacao"]["longitude"])
        localizacao_player = (latitude,longitude)
    except:
        erro = {
            "localizacao":{
                "latitude":"",
                "longitude":""
                }
            }
        return JsonResponse(erro,status=400,safe=False)
    personagens = []
    for i in Objeto_er_map.objects.all():
        localizacao_personagem = (i.latitude,i.longitude)
        distancia = 1000 * distance(localizacao_player, localizacao_personagem).km
        if distancia <= 500: # Mostrar personagens com 500 metros ou menos do jogador
            j = Objeto_er_mapSerializer(i)
            personagens.append(j.data)
    # personagens = Objeto_er_mapSerializer(personagens, many=True)
    data = {
        "personagens":personagens
    }
    return JsonResponse(data,safe=False)