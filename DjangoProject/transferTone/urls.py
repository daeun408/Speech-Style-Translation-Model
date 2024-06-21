from django.urls import path, include
from transferTone import views

urlpatterns = [
    path('', views.translate, name='translate'),
]