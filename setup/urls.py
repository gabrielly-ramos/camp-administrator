"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from camp.views import (
    PilotViewsets,
    CarViewsets,
    TeamViewsets,
    GridViewsets
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pilot/', PilotViewsets.as_view({'get': "list", "post": "create_pilot"})), 
    path('pilot/<int:pk>/', PilotViewsets.as_view({'get': "list", 'put' : 'update_pilot'})), 
    path('car/', CarViewsets.as_view({'get': "list", "post": "create_car"})), 
    path('grid/', GridViewsets.as_view({'get': "list"})), 
    path('team/', TeamViewsets.as_view({'get': "list", "post": "create_team"})),
]
