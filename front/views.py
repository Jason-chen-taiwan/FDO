from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.template import loader


def  front_page(request):
    return render(request, 'front.html')

def usr_login(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return HttpResponse("Login succese")
    else:
        return HttpResponse("Login fail")
    
