from django.urls import path
from .views  import  *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from core.views import login_staff_required
from django.conf import settings

app_name="website_app"
urlpatterns = [
path('',index,name='index'),
path('jogadores/',login_staff_required(Jogadores),name='Jogadores'),
path('jogadores/add/',login_staff_required(JogadorCreate.as_view()),name='Add_Jogador'),
path('jogadores/up/<int:pk>/', login_staff_required(JogadorUpdateView.as_view()), name='Update_Jogador'),
path('jogadores/del/<int:pk>/', login_staff_required(JogadorDeleteView.as_view()), name='Delete_Jogador'),

path('objeto_ers/',login_staff_required(Objeto_ers),name='Objeto_ers'),
path('objeto_ers/add/',login_staff_required(Objeto_erCreate.as_view()),name='Add_Objeto_er'),
path('objeto_ers/up/<int:pk>/', login_staff_required(Objeto_erUpdateView.as_view()), name='Update_Objeto_er'),
path('objeto_ers/del/<int:pk>/', login_staff_required(Objeto_erDeleteView.as_view()), name='Delete_Objeto_er'),

path('objeto_er_maps/',login_staff_required(Objeto_er_maps),name='Objeto_er_maps'),
path('objeto_er_maps/add/',login_staff_required(Objeto_er_mapCreate.as_view()),name='Add_Objeto_er_map'),
path('objeto_er_maps/up/<int:pk>/', login_staff_required(Objeto_er_mapUpdateView.as_view()), name='Update_Objeto_er_map'),
path('objeto_er_maps/del/<int:pk>/', login_staff_required(Objeto_er_mapDeleteView.as_view()), name='Delete_Objeto_er_map'),
]
