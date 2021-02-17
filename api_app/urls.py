from django.urls import path
from .views  import  *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

# *************************************************
from rest_framework import routers
from rest_framework.authtoken import views as auth_token

router = routers.DefaultRouter()
router.register('jogador', JogadorList, 'jogador')
router.register('objeto_er', Objeto_erList, 'objeto_er')
router.register('objeto_er_map', Objeto_er_mapList, 'objeto_er_map')

urlpatterns = router.urls
# *************************************************


app_name="api_app"
urlpatterns +=[
    path('personagens/',personagens_proximos,name='personagens_proximos'),
    path('me/',me,name='me'),
    path('mochila/',mochila,name='mochila'),
    path('job_check_online_users/',job_check_online_users,name='job_check_online_users')
]
