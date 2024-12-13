

from django.urls import path, include

from . import views


urlpatterns = [
   
    path('', views.missing_report, name='report'),
    path('reports/', views.missing_report, name='report'),
    
    path('missing_report/', views.missing_report, name='missing_report'),
    path('aggregate_report/', views.aggregate_report, name='aggregate_report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('years/', views.years, name='years'),
    path('get_report_form/', views.get_report_form, name='get_report_form'),

]