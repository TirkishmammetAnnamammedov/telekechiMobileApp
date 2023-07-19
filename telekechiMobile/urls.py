
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('site-manage/', admin.site.urls),
    path('', include('store.urls')),
    path('auth', obtain_auth_token)
]
