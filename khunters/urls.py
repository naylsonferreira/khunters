from django.contrib import admin
from django.urls import include, path
from website_app.views import login_staff_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_app.urls')),
    path('', login_staff_required(include('website_app.urls'))),
    path('', include('core_app.urls')),
]
