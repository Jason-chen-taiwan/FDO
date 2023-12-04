from django.shortcuts import render

# Create your views here.
def mfg_view(request):
    return render(request, "manufacturer.html")