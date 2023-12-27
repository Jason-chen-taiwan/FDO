from django.http import HttpResponse
from django.shortcuts import render
from rv.models import to0_information
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def rv_view(request):
    return render(request, "rendezvous.html")

@csrf_exempt
def to0_get_api(request):
    if request.method == 'POST':
        guid = request.POST.get('GUID')
        owner_name = request.POST.get('clientusername')
        # 檢查是否有必要的數據
        if guid and owner_name:
            # 創建一個 to0_information 的實例
            to0_info = to0_information(
                guid=guid,
                owner_name=owner_name,
                to0_time=timezone.now()  # 設置當前時間
            )
            
            # 將實例保存到資料庫
            to0_info.save()

            return HttpResponse("數據成功保存。")
        else:
            return HttpResponse("POST 請求中缺少數據。")

    # 如果不是 POST 請求，則返回錯誤響應或重定向
    return HttpResponse("請求方法無效。")

def show_to0_in_api(request):
    # 獲取所有 to0_information 實例
    to0_infos = to0_information.objects.all()

    context = {
        'to0_infos': to0_infos,
        # 其他上下文數據
    }

    return render(request, 'rendezvous.html', context)