from django.template import loader
from django.shortcuts import redirect, render
from .form import login, RegisterForm

def  login_page(request):
    form = login()
    context = {"form":form}
    return render(request, 'login.html',context)

def front_page(request):
    return render(request, 'front.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 这里处理表单数据
            # 如：创建用户、发送验证邮件等
            return redirect('front_page')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})