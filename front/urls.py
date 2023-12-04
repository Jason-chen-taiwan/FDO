from django.urls import path
from . import views

urlpatterns = [
    path("aio", views.aio, name="aio"),
    path("logout", views.logout_view, name="logout"),
    path("manufacturer", views.mfg_view, name="manufacturer"),
    path("rendezvous", views.rv_view, name="rendezvous"),
    path("owner", views.owner_view, name="owner"),
]