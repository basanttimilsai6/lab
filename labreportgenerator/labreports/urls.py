from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.create_report),
    path('doc', views.clinic, name='doc'),
    path('generate-pdf/<int:id>/', views.generate_pdf, name='generate_pdf'),
    path('create_report/', views.create_report, name='create_report'),
    path('view_reports/', views.view_reports, name='view_reports'),
    path('view_reports_detail/<int:id>/', views.view_report_detail, name='view_reports_detail'),
]
