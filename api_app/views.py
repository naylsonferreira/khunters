from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers, viewsets
from .serializers import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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