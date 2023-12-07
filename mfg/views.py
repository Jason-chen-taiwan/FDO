from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import ServerInfoForm, OwnerInfo
from postman.httprequest import post_http_digestAuth, get_http_digestAuth
from django.contrib import messages
from .models import ownerServerInfo

# return context evry time 
def initial_page_context():
    form = ServerInfoForm()
    owner_form = OwnerInfo()
    context = {
        'form': form,
        'owner_form': owner_form
    }
    return context
# Create your views here.
def mfg_view(request):
    if request.method == 'GET':
        form = ServerInfoForm()
        owner_form = OwnerInfo()
        context = {
            'form': form,
            'owner_form': owner_form
        }
    return render(request, "manufacturer.html", context)

def rvinfo_api(request):
    if request.method == 'POST':
        # 获取表单数据
        url = request.POST.get('url', '')  # 第二个参数是默认值，如果没有获取到数据就使用它
        ip = request.POST.get('ip', '')
        port = request.POST.get('port', '')
        # print(url, ip, port)
        api_url = "http://fdosep.ofido.tw:8039/api/v1/rvinfo"
        
        # 基本认证的用户名和密码
        username = 'jasonchen'
        password = 'fjdasoonchen'

        # 使用获取的数据构造请求体
        data = f'[[[5,"{url}"],[3,{port}],[12,2],[2,"{ip}"],[4,{port}]]]'
        # print(data)

        # 发送 POST 请求
        response = post_http_digestAuth(api_url, username, password, data)

        # 检查响应
        if response.ok:
            print('Success!')
            print(response.content)
            # 使用 Django 的 messages 框架来添加成功消息
            messages.success(request, '操作成功！')
        else:
            print('Failed.')
            print(response.status_code)
            # 这里可以处理失败的情况，例如添加错误消息
            messages.error(request, '操作失败。')
        # 重新渲染视图（无论是提交表单还是初始 GET 请求）
        form = ServerInfoForm()  # 或其他逻辑来初始化表单
        return render(request, "manufacturer.html", {'form': form})
    else:
        return HttpResponse ("Invalid http method!")

def owner_credential_get_api(request):
    if request.method == 'POST':

        context = {}

        url = request.POST.get('url', '')
        # print(url)
        username = 'jasonchen'
        password = 'fjdasoonchen'
        response = get_http_digestAuth(url, username, password)
        # 假设服务器返回的是文本或JSON数据
        if response.ok:
            # 假设服务器返回的是文本
            context = initial_page_context()
            context['owner_credential'] = response.content.decode('utf-8')
            return render(request, 'manufacturer.html', context)
        else:
            context['owner_credential'] = '请求失败，状态码：' + str(response.status_code)
            return HttpResponse(context)


def owner_credential_save_api(request):
    if request.method == 'POST':
        owner_credential = request.POST.get('owner_credential', '')
        ownername = request.POST.get('ownername', '')
        # 创建新的 ownerServerInfo 实例
        new_owner_server_info = ownerServerInfo(
            serverName=ownername, 
            credential=owner_credential
        )
        new_owner_server_info.save()
        context = initial_page_context()
        context['owner_credential_save_status']="成功"
        return render(request, 'manufacturer.html', context)