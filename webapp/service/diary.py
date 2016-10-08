from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from webapp.models import *


def getalldirys(request):
    request.encoding = 'utf-8'
    diarys = Diary.objects.all()
    if not diarys:
        return JsonResponse({"status": "fail", "msg": "日记列表为空"})
    else:
        diarylist = serializers.serialize("json", diarys)
        return HttpResponse(diarylist, content_type="application/json")
