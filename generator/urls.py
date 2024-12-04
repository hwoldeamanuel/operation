
from django.urls import path, include

from . import views


urlpatterns = [
   
    path('', views.generators, name='generators'),
    path('generators/', views.generators, name='generators'),



]