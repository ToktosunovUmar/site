from django.shortcuts import render
from . import models


def filter_view(request):
    if request.method == 'GET':
        for_adult = models.CLOTH.objects.filter(tags__name='для взрослых').order_by('-id')
        for_old = models.CLOTH.objects.filter(tags__name='для пенсионеров').order_by('-id')
        for_kids = models.CLOTH.objects.filter(tags__name='для детей').order_by('-id')

        return render(
            request,
            template_name='filter.html',
            context={
                'for_adult': for_adult,
                'for_old': for_old,
                'for_kids': for_kids
            }
        )
