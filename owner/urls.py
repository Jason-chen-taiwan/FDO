from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.owner_view, name='owner')
]