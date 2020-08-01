from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .serializers import *
import os
import json

@csrf_exempt
def singup_json(request):
    try:
        dados = json.loads(request.body)
        email = dados['email']
        password = dados['email']
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

    new_user = User(username=email,email=email,password=password)    
    try:
        new_user.save()
    except:
        resultado={'email':'E-mail já cadastrado'}
        return JsonResponse(resultado,safe=False,status=400)
    saved_user = User.objects.get(email=email)
    serializer = UserSerializer(saved_user)
    
    token = Token(user=saved_user)
    token.save()
    token = Token.objects.get(user=saved_user)

    result = serializer.data
    result = {
        'id': result["id"],
        'email': result["email"],
        'first_name': result["first_name"],
        'last_name': result["last_name"],
        'token':token.key
        }
    return JsonResponse(result,safe=False)

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
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'core/singup.html', {'form': form})

def profile(request):
    sucesso = False
    if request.method == 'POST':
        form_user = UserForm(request.POST,instance=request.user)
        form_profile = ProfileForm(request.POST,instance=request.user.profile)
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            user_up = request.user
            user_up.username = request.user.email
            user_up.save()
            sucesso = True
    
    form_user = UserForm(instance=request.user)
    form_profile = ProfileForm(instance=request.user.profile)
    contexto = {
        "form_user": form_user,
        "form_profile": form_profile,
        "sucesso":sucesso
    }
    return render(request, 'core/profile.html', contexto)
def profile_json(request):
    if request.method == 'POST':
        pass
    else:
        user = UserSerializer(request.user)
        profile = ProfileSerializer(request.user.profile)
        contexto = {
            "user":user.data,
            "profile":profile.data
        }
        return JsonResponse(contexto,safe=False)
def list_users(request):
    if not request.user.is_staff:
        return redirect('/')
    users = User.objects.all().order_by('email','first_name', 'last_name')
    paginator = Paginator(users, 30)
    page = request.GET.get('page')
    users_ = paginator.get_page(page)
    contexto = {
        "users": users_,
    }
    return render(request, 'core/list_users.html', contexto)

def list_users_json(request):
    if not request.user.is_staff:
        return JsonResponse({"error":"acesso negado"},status=401)
    users = User.objects.all().order_by('email','first_name', 'last_name')
    users = UserSerializer(users,many=True)
    profiles = Profile.objects.all()
    profiles = ProfileSerializer(profiles,many=True)
    contexto = {
        "users": users.data,
        "profiles":profiles.data
    }
    return JsonResponse(contexto,safe=False)