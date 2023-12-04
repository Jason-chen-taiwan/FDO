from django.urls import path, include
from . import views

urlpatterns = [
    path("aio", views.aio, name="aio"),
    path("logout", views.logout_view, name="logout"),
    path("manufacturer/", include("mfg.urls")),
    path("rendezvous/", include("rv.urls")),
    path("owner/", include("owner.urls")),
]