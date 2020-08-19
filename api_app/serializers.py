from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from website_app.models import *

class Objeto_erSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto_er
        fields = "__all__"

class Objeto_er_mapSerializer(serializers.ModelSerializer):
    prefab = serializers.SerializerMethodField()
    tamanho = serializers.SerializerMethodField()
    class Meta:
        model = Objeto_er_map
        fields = "__all__"
    def get_prefab(self, obj):
        return obj.objeto_er.personagem.prefab
    def get_tamanho(self, obj):
        return obj.objeto_er.personagem.tamanho

class CapturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captura
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","first_name","last_name"]

class JogadorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Jogador
        fields = "__all__"