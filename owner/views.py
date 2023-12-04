from django.shortcuts import render

# Create your views here.


def owner_view(request):
    return render(request, "owner.html")