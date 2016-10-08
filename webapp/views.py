from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from webapp.models import *
import json


def diary(request):
    u = request.COOKIES.get('user', '')
    if not u:
        result = {'islogin': False}
        return render(request, 'hello.html', {
            'result': json.dumps(result)
        })
    u = eval(u)
    request.session['user'] = u
    mydiarys = serializers.serialize("json", Diary.objects.filter(userid=u['id']))
    if (u['relationid'] != None):
        shediarys = serializers.serialize("json", Diary.objects.filter(userid=u['relationid']))
        result = {'islogin': True, 'mydiarylist': mydiarys, 'shediarys': shediarys}
        responserender = render(request, 'hello.html', {'result': json.dumps(result)})
        responserender.set_cookie('user', u)
        return responserender
    result = {'islogin': True, 'mydiatylist': mydiarys}
    responserender = render(request, 'hello.html', {'result': json.dumps(result)})
    responserender.set_cookie('user', u)
    return responserender


