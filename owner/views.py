import json
import os
from django.http import HttpResponse
from django.shortcuts import render
import requests
from mfg.forms import ServerInfoForm
from postman.httprequest import post_http_digestAuth,get_http_digestAuth
# Create your views here.
from mfg.views import initial_page_context
from .models import machine
from django.utils.dateparse import parse_datetime

def owner_view(request):
    form = ServerInfoForm()  # 或其他逻辑来初始化表单
    contex = {
            'form':form
        }
    return render(request, "owner.html",contex)

def RVBlod_TO2_deriction_api(request):
    if request.method == 'POST':
        # 获取表单数据
        dns = request.POST.get('url', '')  # 第二个参数是默认值，如果没有获取到数据就使用它
        ip = request.POST.get('ip', '')
        port = request.POST.get('port', '')
        # print(url, ip, port)
        api_url = 'http://fdosep.ofido.tw:8042/api/v1/owner/redirect'
        
        # 获取环境变量
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        # 使用获取的数据构造请求体
        data = f'[["{ip}","{dns}",{port},3]]'
        # print(data)

        # 发送 POST 请求
        response = post_http_digestAuth(api_url, username, password, data)
        form = ServerInfoForm()  # 或其他逻辑来初始化表单
        contex = {
            'form':form
        }
        # 检查响应
        if response.ok:
            print('Success!')
            contex['status'] = 'Success'
        else:
            print('Failed.')
            print(response.status_code)
            # 这里可以处理失败的情况，例如添加错误消息
            contex['status'] = 'fail'
        # 重新渲染视图（无论是提交表单还是初始 GET 请求）
       
        return render(request, "owner.html", contex)
    else:
        return HttpResponse ("Invalid http method!")

def get_all_list_machine_api(request):
    if request.method == 'POST':
        url = 'http://fdosep.ofido.tw:8042/api/v1/owner/vouchers'
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        response = get_http_digestAuth(url, username, password)
        print(response.content.decode('utf-8'))
        response_text = response.content.decode('utf-8')
        # 使用 .json() 方法解析 JSON 数据
        list_guid = response_text.strip().split('\n')
        context = initial_page_context()
        context['list_guid']=list_guid
        return render(request, "owner.html", context)

def trigger_to0_api(request):
    if request.method == 'POST':
        guid = request.POST.get('GUID')
        clientusername = request.POST.get('clientusername')
        # 构建要触发的 API URL
        api_url = 'http://127.0.0.1:8000/front/rendezvous/api/to0_in'
         # 准备 POST 请求的数据
        data = {
            'GUID': guid,
            'clientusername': clientusername,  
        }
        # 发送 POST 请求
        response = requests.post(api_url, data=data)
        if response.ok:
            print('rv_to0_information send ok')
        else:
            print('rv_to0_information send fail')
        url = f'https://fdosep.ofido.tw:8043/api/v1/to0/{guid}'
        # print(url)
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        response = get_http_digestAuth(url, username, password)
        contex = initial_page_context()
        if response.ok:
            print('Success!')
            contex['TO0status'] = 'Success'
        else:
            print('Failed.')
            print(response.status_code)
            # 这里可以处理失败的情况，例如添加错误消息
            contex['TO0status'] = 'fail'
        # 重新渲染视图（无论是提交表单还是初始 GET 请求）
       
        return render(request, "owner.html", contex)

def machine_status_api(request):
    if request.method == 'POST':
        guid = request.POST.get('GUID')
        ownername = request.POST.get('clientusername')
        url = f'http://fdosep.ofido.tw:8042/api/v1/owner/state/{guid}'
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        # 假设 response 是您通过 get_http_digestAuth 获得的响应对象
        response = get_http_digestAuth(url, username, password)
        # 将响应内容从字节字符串转换为普通字符串
        response_str = response.content.decode('utf-8')

        # 解析 JSON 数据
        try:
            response_data = json.loads(response_str)
        except json.JSONDecodeError:
            # 如果响应内容不是有效的 JSON，只显示字符串
            return HttpResponse("Invalid JSON response")

        # 从响应中提取数据
        to0_expiry = response_data.get('to0Expiry')
        to2_completed_on = response_data.get('to2CompletedOn')

        # 将字符串格式的时间戳转换为 datetime 对象
        to0_timestamp = parse_datetime(to0_expiry) if to0_expiry else None
        to2_timestamp = parse_datetime(to2_completed_on) if to2_completed_on else None
        context = initial_page_context()
        
        # 创建或更新 machine 实例
        machine_obj, created = machine.objects.update_or_create(
            guid=guid,
            defaults={
                'to0_timestamp': to0_timestamp,
                'to2_timestamp': to2_timestamp,
                'owner': ownername
            }
        )
        # 您可以进一步格式化 response_data 以适应您的需求
        # 例如，如果您知道响应数据是一个字典，您可以选择性地提取某些字段
        # 以下代码假设 response_data 是一个字典
        formatted_response = ""
        if isinstance(response_data, dict):
            for key, value in response_data.items():
                formatted_response += f"{key}: {value}\n"
        else:
            # 如果响应数据不是字典，直接使用字符串
            formatted_response = response_data

        context['machine_status'] = formatted_response
        return render(request, "owner.html", context)

def all_machine_status_api(request):
    if request.method == 'POST':
        machines = machine.objects.all()  # 获取所有 machine 对象
        context = initial_page_context()
        context['machines'] = machines
        
        return render(request, 'owner.html', context)
    else:
        # 如果不是 POST 请求，可以重定向或返回一个不同的页面
        return render(request, 'owner.html')