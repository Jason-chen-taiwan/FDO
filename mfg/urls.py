from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.mfg_view, name='manufacturer'),
    path('api/v1/rvinfopull/', views.rvinfo_api, name='rv_info')
]