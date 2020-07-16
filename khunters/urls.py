from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('c846b9ced21cc3780dbe14cce3f24574/admin/', admin.site.urls),
    path('c846b9ced21cc3780dbe14cce3f24574/api/',include('api_app.urls')),
    path('c846b9ced21cc3780dbe14cce3f24574/',include('website_app.urls')),
]