from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.urls import reverse
from . import models, forms
from django.views import generic


@method_decorator(cache_page(60 * 15), name='dispatch')
class Searchbookview(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_post_object'
    paginate_by = 5

    def get_queryset(self):
        return models.books_post.objects.prefetch_related('review_book').\
            filter(tittle__icontains=self.request.GET.get('q')).all().order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class Editbookview(generic.ListView):
    template_name = 'crud/edit_book.html'
    context_object_name = 'book_edit_object'
    model = models.books_post

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all().order_by('-id')


@method_decorator(cache_page(60 * 15), name='dispatch')
class Updateview(generic.UpdateView):
    template_name = 'crud/update_book.html'
    form_class = forms.book_Form
    success_url = '/book_edit_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.books_post, id=book_id)

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


# def edit_book_view(request):
#    if request.method == "GET":#
#       book_edit_object = models.books_post.objects.all()
#       return render(
#           request,
#           template_name='crud/edit_book.html',
#           context={
#               'book_edit_object': book_edit_object
#           }
#       )
#
#
# def update_view(request, id):
#    book_id = get_object_or_404(models.books_post, id=id)
#    if request.method == 'POST':
#        form = forms.book_Form(request.POST, instance=book_id)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('Книга отредоктирована!!! <a href = "/book_post_list/">На список книг</a>')
#    else:
#        form = forms.book_Form(instance=book_id)
#
#    return render(
#        request,
#        template_name='crud/update_book.html',
#        context={
#            'form': form,
#            'book_id': book_id
#        }
#    )

@method_decorator(cache_page(60 * 15), name='dispatch')
class Deletebookview(generic.ListView):
    template_name = 'crud/delete_book.html'
    context_object_name = 'book_delete_object'
    model = models.books_post

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


@method_decorator(cache_page(60 * 15), name='dispatch')
class Bookdropview(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/book_delete_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.books_post, id=book_id)

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


# def delete_book_view(request):
#    if request.method == "GET":
#        book_delete_object = models.books_post.objects.all()
#        return render(
#            request,
#            template_name='crud/delete_book.html',
#            context={
#                'book_delete_object': book_delete_object
#            }
#        )
#
#
# def book_drop_view(request, id):
#    book_id = get_object_or_404(models.books_post, id=id)
#    book_id.delete()
#    return HttpResponse('Книга удалены!!! <a href = "/book_post_list/">На список книг</a>')

@method_decorator(cache_page(60 * 15), name='dispatch')
class Addbookview(generic.CreateView):
    template_name = 'crud/book_add.html'
    form_class = forms.book_Form
    success_url = '/book_post_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Addbookview, self).form_valid(form=form)

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


# def add_book_view(request):
#    if request.method == 'POST':
#        form = forms.book_Form(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('Данные успешно отправлены!!! <a href = "crud/book_add.html">На список книг</a>')
#    else:
#        form = forms.book_Form()
#    return render(
#        request,
#        template_name='crud/book_add.html',
#        context={
#            'form': form
#        }
#    )

@method_decorator(cache_page(60 * 15), name='dispatch')
class Bookdetailview(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.books_post, id=book_id)

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


# def book_detail_view(request, id):
#    if request.method == 'GET':
#        book_id = get_object_or_404(models.books_post, id=id)
#        return render(
#            request,
#            template_name='book_detail.html',
#            context={
#                'book_id': book_id
#            }
#        )

@method_decorator(cache_page(60 * 15), name='dispatch')
class Booklistview(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_post_object'
    model = models.books_post

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


# def book_list_view(request):
#    if request.method == "GET":
#        book_post_object = models.books_post.objects.all()
#        return render(
#            request,
#            template_name='book_list.html',
#            context={
#                'book_post_object': book_post_object
#            }
#        )


def info_view(request):
    return HttpResponse('Мое имя Токтосунов Умар')


def info_friend_view(request):
    return HttpResponse('Имя моего друга ')


def time_view(request):
    time = datetime.datetime.now()
    return HttpResponse(time.strftime("%H:%M:%S"))
