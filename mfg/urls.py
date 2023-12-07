from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.mfg_view, name='manufacturer'),
    path('api/v1/rvinfopull/', views.rvinfo_api, name='rv_info'),
    path('api/v1/getownercredential/', views.owner_credential_get_api, name='getownercredential'),
    path('api/v1/ownercredentialsave/', views.owner_credential_save_api, name='ownercredentialsave'),
]