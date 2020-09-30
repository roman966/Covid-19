from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('basic/', views.basic, name='basic'),
    path('info/', views.information, name='info'),
    path('addi/', views.additional, name='additional'),
    path('records/', views.records, name='records'),
    path('final/', views.final, name='final'),
]
