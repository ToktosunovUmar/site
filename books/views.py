from django.shortcuts import render
from django.http import HttpResponse
import datetime


def info_view(request):
    return HttpResponse('Мое имя Токтосунов Умар')


def info_friend_view(request):
    return HttpResponse('Имя моего друга ')


def time_view(request):
    time = datetime.datetime.now()
    return HttpResponse(time.strftime("%H:%M:%S"))
