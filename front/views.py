from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.template import loader
from django.views.decorators.http import require_POST
from front.models import UserProfile

def aio(request):
    context = {}
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            context['identity'] = user_profile.identity
        except UserProfile.DoesNotExist:
            context['identity'] = None
    print(context)
    return render(request, 'aio.html', context)

@require_POST
def logout_view(request):
    logout(request)
    # 重定向到首页或登录页面
    return redirect('../front')  # 请替换为合适的 URL 名称
    

