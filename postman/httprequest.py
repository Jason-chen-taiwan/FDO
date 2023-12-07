import requests
from requests.auth import HTTPDigestAuth


def post_http_digestAuth(url,username, password, data):
    # 发送 POST 请求
    response = requests.post(
        url,
        auth=HTTPDigestAuth(username, password),
        headers={'Content-Type': 'text/plain'},
        data=data
    )

    return response

def get_http_digestAuth(url, username, password, params=None):
    # 发送 GET 请求
    response = requests.get(
        url,
        auth=HTTPDigestAuth(username, password),
        params=params  # URL 参数
    )

    return response