from django.urls import path, include
from .import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('post', views.PostView)

urlpatterns = [
    path('', include(routers.urls))
]
