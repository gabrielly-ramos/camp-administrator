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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from camp import views
from camp.views import (
    PilotViewset, 
    CarViewset,    
    TeamViewset,
    GridViewset
    )
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pilot', views.PilotViewset)
router.register(r'car', views.CarViewset)
router.register(r'team', views.TeamViewset)
router.register(r'grid', views.GridViewset)
urlpatterns = router.urls

# urlpatterns = [
#     path('admin/', admin.site.urls),    
#     path('pilot/', PilotViewsets.as_view({'get': "list", "post": "create_pilot"})), 
#     path('pilot/<int:pk>/', PilotViewsets.as_view({'get': "list", 'put' : 'update_pilot'})), 
#     path('car/', CarViewset.as_view({'get': "list", "post": "create_car"})), 
#     path('grid/', GridViewsets.as_view({'get': "list"})), 
#     path('team/', TeamViewsets.as_view({'get': "list", "post": "create_team"})),
#     path('', include(router.urls)),
# ]
