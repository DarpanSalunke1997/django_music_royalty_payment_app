from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.upload_file),
    path('csv/', views.export_CSV, name='csv'),
    path('json/', views.export_JSON, name='json'),
    path('xls/', views.export_XLS, name='xls'),
    
]
