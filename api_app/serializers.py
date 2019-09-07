from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from website_app.models import *

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = "__all__"

class Objeto_erSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto_er
        fields = "__all__"

class Objeto_er_mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto_er_map
        fields = "__all__"

class CapturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captura
        fields = "__all__"