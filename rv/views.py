from django.shortcuts import render

# Create your views here.

def rv_view(request):
    return render(request, "rendezvous.html")