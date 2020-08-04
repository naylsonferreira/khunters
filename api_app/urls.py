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
router.register('captura', CapturaList, 'captura')

urlpatterns = router.urls
# *************************************************
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
for user in User.objects.all():
    Token.objects.get_or_create(user=user)

app_name="api_app"
urlpatterns +=[
    path('personagens/',personagens_proximos,name='personagens_proximos')
]
