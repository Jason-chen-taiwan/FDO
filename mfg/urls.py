from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.mfg_view, name='manufacturer'),
    path('api/v1/rvinfopull/', views.rvinfo_api, name='rv_info'),
    path('api/v1/getownercredential/', views.owner_credential_get_api, name='getownercredential'),
    path('api/v1/ownercredentialsave/', views.owner_credential_save_api, name='ownercredentialsave'),
    path('api/v1/ownercredentiallist/', views.get_ownerseerver_list, name='ownercredentiallist'),
    path('api/v1/clientmslist/', views.client_ms_list_api, name='clientMsList'),
    path('api/v1/dimachinelist/', views.list_all_client_api, name='dimachinelist'),
    path('api/v1/showownerserialno/', views.show_all_ownerCredential_serialNo_api, name='showOwnerAndSerialNo'),
    path('api/v1/makeOwnershipVoucher_api/', views.makeOwnershipVoucher_api, name='makeOwnershipVoucher'),
    path('api/v1/ownershipvoucherlist/', views.ownership_voucher_list_api, name='ownership_voucher_list'),
    path('api/v1/sendownership/', views.sendownership_api, name='sendownership'),
]