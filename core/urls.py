from django.urls import path,include,reverse_lazy
from .views import  *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile/json', ProfileJson, 'profile_json')

app_name="core"
urlpatterns = [
    path('login/json/',login_json,name='login_json'),
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html",redirect_authenticated_user=True),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="core/logout.html"),name='logout'),
    path('singup/json/',singup_json,name='singup_json'),
    path('singup/',singup,name='singup'),
    path('profile/up/<int:pk>/', login_required(ProfileUpdateView.as_view()), name='Update_profile'),
    path('profile/',login_required(ProfileListView.as_view()),name='profile'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name="core/password_change_form.html",
            success_url = reverse_lazy('core:password_change_done')
        ),name='password_change'),
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name="core/password_change_done.html"
        ),name='password_change_done'),
    path('password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name="core/password_reset_form.html",
            email_template_name = "core/password_reset_email.html",
            success_url = reverse_lazy('core:password_reset_done')
        ),name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="core/password_reset_done.html"
        ),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="core/password_reset_confirm.html",
            success_url = reverse_lazy('core:password_reset_complete')
        ),name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="core/password_reset_complete.html"),
            name='password_reset_complete'
        ),
    path('api/', include(router.urls)),
    path('',include(settings.DEFAULT_APP+'.urls',namespace=settings.DEFAULT_APP)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)