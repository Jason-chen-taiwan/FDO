from django.db import IntegrityError
from django.template import loader
from django.shortcuts import redirect, render
from .form import LoginForm, RegisterForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from front.models import UserProfile

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)

            if user is not None:
                login(request, user)
                # 重定向到成功登录后的页面
                return redirect('../front/aio')
            else:
                # 添加错误消息
                form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def front_page(request):
    return render(request, 'front.html')

# @require_http_methods(['POST'])
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            identity = form.cleaned_data['identity']

            # 检查用户名是否已存在
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')
                return render(request, 'register.html', {'form': form})  # 重新渲染页面并显示错误
            else:
                try:
                    # 创建新用户
                    user = User.objects.create_user(username, email, password)
                    # 获取身份信息并创建 UserProfile
                    identity = form.cleaned_data['identity']
                    user_profile = UserProfile(user=user, identity=','.join(identity))
                    user_profile.save()
                    # 重定向到前端页面或登录页面
                    return redirect('front')
                except IntegrityError:
                    form.add_error('username', 'Username already exists')
                    return render(request, 'register.html', {'form': form})  # 重新渲染页面并显示错误
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
