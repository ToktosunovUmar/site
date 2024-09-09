from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.books_post, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id
            }
        )


def book_list_view(request):
    if request.method == "GET":
        book_post_object = models.books_post.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'book_post_object': book_post_object
            }
        )


def info_view(request):
    return HttpResponse('Мое имя Токтосунов Умар')


def info_friend_view(request):
    return HttpResponse('Имя моего друга ')


def time_view(request):
    time = datetime.datetime.now()
    return HttpResponse(time.strftime("%H:%M:%S"))
