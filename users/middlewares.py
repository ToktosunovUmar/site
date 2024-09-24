from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class WorkHiringMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            exp = int(request.POST.get('exp'))
            if exp < 1:
                HttpResponseBadRequest('У вас слишком мало опыта!!')
            elif exp >= 1 and exp <= 2:
                request.club = 'junior'
            elif exp >= 2 and exp <= 5:
                request.club = 'middle'
            elif exp >= 5 and exp <= 8:
                request.club = 'Senior'
            else:
                return HttpResponseBadRequest("У вас либо слишком много опыта "
                                              "или вы нам не подходите ")
        elif request.path == request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Опыт не определен')
