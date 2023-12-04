from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.rv_view, name='rv')
]