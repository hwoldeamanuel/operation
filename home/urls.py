

from django.urls import path, include

from . import views


urlpatterns = [
   
    path('', views.missing_report, name='report'),
    path('reports/', views.missing_report, name='report'),
    
    path('missing_report/', views.missing_report, name='missing_report'),
    path('aggregate_report/', views.aggregate_report, name='aggregate_report'),
    path('dashboard/', views.dashboard, name='dashboard'),

]