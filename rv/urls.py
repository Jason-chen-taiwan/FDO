from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.rv_view, name='rv'),
    path('api/to0_in', views.to0_get_api, name='to0get'),
    path('api/to0_in_list', views.show_to0_in_api, name='listallto0'),
]