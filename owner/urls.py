from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.owner_view, name='owner'),
    path('api/to2deriction', views.RVBlod_TO2_deriction_api, name='to2deriction'),
    path('api/allguid', views.get_all_list_machine_api, name='allguid'),
    path('api/triggerto0', views.trigger_to0_api, name='triggerto0'),
    path('api/machinestatus', views.machine_status_api, name='machinestatus'),
    path('api/allmachinestatus', views.all_machine_status_api, name='showallmachinestatus'),
]