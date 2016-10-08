from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response
from django.utils import log

from webapp.models import *
import json


def loginajax(request):
    request.encoding = 'utf-8'
    context = {}
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        u = User.objects.filter(username=username).filter(password=password)[:1]
        if not u:
            context = {"status": "fail", "msg": "用户名或密码错误"}
            return JsonResponse(context)
        else:
            u = u[0].toJSON()
            u['password'] = "******"
            request.session['user'] = u
            context = {"status": "ok", "msg": "login success", "obj": u}
            response = JsonResponse(context)
            response.set_cookie('user', u)
            return response
    else:
        return JsonResponse({"status": "fail", "msg": "参数错误"})


def testsession(request):
    u = request.session['user']
    print("-----")
    print(u)
    u1 = request.COOKIES.get('user', '')
    print(u1)
    print("-----")
    return JsonResponse({"status": "fail", "msg": "参数错误"})


def logout(request):
    response = render(request, 'logout.html')
    # 清理cookie里保存username
    response.delete_cookie('user')
    del request.session['user']
    print("退出")
    return response
