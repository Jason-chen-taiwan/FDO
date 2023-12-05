from django.http import HttpResponse
from django.shortcuts import render
from .forms import ServerInfoForm, OwnerInfo
import requests
from requests.auth import HTTPDigestAuth


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
        print(data)

        # 发送 POST 请求
        response = requests.post(
            api_url,
            auth=HTTPDigestAuth(username, password),
            headers={'Content-Type': 'text/plain'},
            data=data
        )

        # 检查响应
        if response.ok:
            print('Success!')
            print(response.content)
        else:
            print('Failed.')
            print(response.status_code)

        return HttpResponse ("Hello world!")
    else:
        return HttpResponse ("Invalid http method!")