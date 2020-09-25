from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse,HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .forms import *
from .serializers import *
import os
import json


@csrf_exempt
def login_json(request):
    resultado = {
        "error":"Campos obrigatorios faltando",
        "campos":{"email":"","password":""}
        }
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            email = dados['email']
            password = dados['password']
        except:
            email = request.POST.get('email')
            password = request.POST.get('password')
        
        try:
            user = authenticate(username=email, password=password)
        except:
            user = None;
    
        if user is not None:
            Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=user)
            return JsonResponse({ 'token':token.key },safe=False)
        resultado = {
            "error":"Credenciais invalidas",
            "campos":{"email":"","password":""}
            }
    return JsonResponse(resultado,safe=False,status=400)

@csrf_exempt
def singup_json(request):
    try:
        dados = json.loads(request.body)
        email = dados['email']
        password = dados['password']
    except:
        email = request.POST.get('email')
        password = request.POST.get('password')
    
    if not email or not password:
        resultado = {
            "error":"campos obrigatorios faltando",
            "campos":{
                "email":"",
                "password":""
                }
            }
        return JsonResponse(resultado,safe=False,status=400)

    try:
        validate_email(email)
    except:
        resultado={'email':'E-mail inválido'}
        return JsonResponse(resultado,safe=False,status=400)
    new_user = User(username=email)
    new_user.set_password(password)
    try:
        new_user.save()
    except:
        resultado={'email':'E-mail já cadastrado'}
        return JsonResponse(resultado,safe=False,status=400)
    
    saved_user = User.objects.get(username=email)
    Token.objects.get_or_create(user=saved_user)
    token = Token.objects.get(user=saved_user)
    return JsonResponse({ 'token':token.key },safe=False)

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            try:
                validate_email(username)
            except:
                erros={
                    'email':'Por favor digite um Email valido'
                }
                return render(request, 'core/singup.html', {'form': form, 'erros':erros})
            form.save()            
            user = authenticate(username=username, password=raw_password)
            user.email = user.username
            user.save()
            Token.objects.get_or_create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'core/singup.html', {'form': form})

class ProfileJson(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileListView(ListView):
    model = Profile
    paginate_by = 10
    ordering = 'email'

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = [
        'email',
        'nome',
        'apelido',
        'foto',
        'sobre',
        'whatsapp',
        'instagram',
        'idade',
        'genero'
        ]
    template_name = 'core/form.html'
    
    def dispatch(self, request, *args, **kwargs):
        instancia = self.get_object()
        if instancia.user.pk != request.user.pk and not request.user.is_superuser:
            return redirect(instancia)
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

def login_staff_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_staff,
        login_url="/",
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator