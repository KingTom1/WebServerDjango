from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import requests
from django.http import JsonResponse
import json
# Create your views here.
@require_http_methods(["GET"])
def show_user(request):
    books = requests.get("http://127.0.0.1:9999/show_user")
    # response['list'] = books.text
    # print(response)
    response = books.text
    print(response)
    return JsonResponse(json.loads(response))

@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        username = request.GET.get('add_user')
        print(username)
        url = "http://127.0.0.1:9999/add_user/?add_user="+username
        print(url)
        requests.get(url)

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
