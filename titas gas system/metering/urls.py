from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-station/', views.add_station, name='add_station'),
    path('add-run/', views.add_metering_run, name='add_metering_run'),
    path('add-reading/', views.add_monthly_reading, name='add_monthly_reading'),
    
    # একদম শেষে এই নতুন লাইনটি যুক্ত হলো
    path('ajax/load-metering-runs/', views.load_metering_runs, name='ajax_load_metering_runs'),
]
