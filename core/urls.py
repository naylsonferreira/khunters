from django.urls import path,include,reverse_lazy
from .views  import  *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as auth_token

app_name="core" #deixar comentado
urlpatterns = [
    path('login/json/', auth_token.obtain_auth_token,name='login_json'),
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html",redirect_authenticated_user=True),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="core/logout.html"),name='logout'),
    path('singup/json/',singup_json,name='singup_json'),
    path('singup/',singup,name='singup'),
    path('profile/json/',login_required(profile_json),name='profile_json'),
    path('profile/',login_required(profile),name='profile'),
    path('users/json/',login_required(list_users_json),name='list_users_json'),
    path('users/',login_required(list_users),name='list_users'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name="core/password_change_form.html",success_url = reverse_lazy('core:password_change_done')),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name="core/password_change_done.html"),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="core/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset_complete.html"), name='password_reset_complete'),
    path('',include(settings.DEFAULT_APP+'.urls',namespace=settings.DEFAULT_APP)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
