from django.shortcuts import render

# Create your views here.

def rv_view(request):
    return render(request, "rendezvous.html")

def to0_get(request):
    if request.method == 'POST':
        guid = request.POST.get('GUID')
        owner_name = request.POST.get('clientusername')