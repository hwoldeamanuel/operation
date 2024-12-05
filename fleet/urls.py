

from django.urls import path, include

from . import views


urlpatterns = [
   
    path('', views.fleets, name='fleets'),
    path('fleets/', views.fleets, name='fleets'),
    path('fleet_list/', views.fleet_list, name='fleet_list'),
    path('fleet/<int:id>/', views.fleet, name='fleet'),
    path('edit_fleet/<int:id>/', views.edit_fleet, name='edit_fleet'),
    path('edit_fleet_log/<int:id>/', views.edit_fleet_log, name='edit_fleet_log'),
    path('fleet/add/', views.add_fleet, name='add_fleet'),
    path('fleet_filter/', views.fleet_filter, name='fleet_filter'),
    path('fleet_log/add/<int:id>/', views.add_fleet_log, name='add_fleet_log'),
    path('download_log_sheet/<int:id>/', views.download_logsheet, name='download_logsheet'),
    path('generators/', views.generators, name='generators'),



]