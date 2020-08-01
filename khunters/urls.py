from django.contrib import admin
from django.urls import include,path

t = 'c846b9ced21cc3780dbe14cce3f24574'

urlpatterns = [
    path('admin', admin.site.urls),
    path('api',include('api_app.urls')),
    path('',include('core.urls')),
]