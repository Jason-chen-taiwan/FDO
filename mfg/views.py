import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import ServerInfoForm, OwnerInfo
from postman.httprequest import post_http_digestAuth, get_http_digestAuth
from django.contrib import messages
from .models import ownerServerInfo, ClientMachine
from dotenv import load_dotenv
from datetime import datetime
import os

# load .env
load_dotenv()

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
        
        # 获取环境变量
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

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
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
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
        rpusername = request.POST.get('rpusername')
        # 创建新的 ownerServerInfo 实例
        new_owner_server_info = ownerServerInfo(
            serverName=ownername, 
            credential=owner_credential,
            rpbelong = rpusername
        )
        new_owner_server_info.save()
        context = initial_page_context()
        context['owner_credential_save_status']="成功"
        return render(request, 'manufacturer.html', context)

def get_ownerseerver_list(request):
    if request.method =='POST':
        # 获取所有ownerServerInfo实例
        username = request.POST.get('rpusername', '')
        print(username)
        all_owner_server_info = ownerServerInfo.objects.filter(rpbelong=username)

        # 将查询结果传递给模板
        context = initial_page_context()
        context['owner_servers'] = all_owner_server_info
        return render(request, 'manufacturer.html', context)

def client_ms_list_api(request):
    if request.method =='POST':
        seconds = request.POST.get('seconds', '')
        clientusername =  request.POST.get('clientusername', '')
        print(seconds)
        url = f'https://fdosep.ofido.tw:8038/api/v1/deviceinfo/{seconds}'
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        response = get_http_digestAuth(url, username, password)
        print(response.content.decode('utf-8'))

        # 使用 .json() 方法解析 JSON 数据
        data = response.json()
        
        context = initial_page_context()

        save_status = []
       # 遍历解析后的数据
        for item in data:
            try:
                serial_no = item.get('serial_no', '')
                guid = item.get('uuid', '')
                timestamp = item.get('timestamp', '')
                alias = item.get('alias', '')

                # 将字符串格式的时间戳转换为 datetime 对象
                di_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

                # 创建 ClientMachine 实例
                client_machine, created = ClientMachine.objects.get_or_create(
                    guid=guid,
                    defaults={
                        'serial_no': serial_no,
                        'di_timestamp': di_timestamp,
                        'attestation_type': alias,
                        'clientbelong' : clientusername
                    }
                )
                
                # 如果实例已存在并且有更新，可以在这里更新相应的字段
                if not created:
                    client_machine.serial_no = serial_no
                    client_machine.di_timestamp = di_timestamp
                    client_machine.attestation_type = alias
                    client_machine.clientbelong = clientusername
                    client_machine.save()
                    save_status.append(f"{guid} update succese")
                else:
                    save_status.append(f"{guid} create succese")
            except:
                save_status.append(f"{guid} faild")
        context['owner_status']=save_status
        return render(request, 'manufacturer.html', context)

def list_all_client_api(request):
    if request.method =='POST':
        # 获取所有ownerServerInfo实例
        clientusername = request.POST.get('clientusername', '')
        print(clientusername)
        all_client_machine_info = ClientMachine.objects.filter(clientbelong=clientusername)

        print(all_client_machine_info)
        # 将查询结果传递给模板
        context = initial_page_context()
        context['client_machine'] = all_client_machine_info
        return render(request, 'manufacturer.html', context)