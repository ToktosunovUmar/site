from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60 * 15), name='dispatch')
class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = forms.CustomRegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        exp = form.cleaned_data['exp']
        if exp < 1:
            self.object.club = 'Мало опыта!!'
        elif exp >= 1 and exp <= 2:
            self.object.club = 'jun'
        elif exp >= 2 and exp <= 5:
            self.object.club = 'midd'
        elif exp >= 5 and exp <= 8:
            self.object.club = 'Sen'
        else:
            self.object.club = 'Опыт не определен!!!!'
        self.object.save()
        return response

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


@method_decorator(cache_page(60 * 15), name='dispatch')
class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse('users:user_list')

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


@method_decorator(cache_page(60 * 15), name='dispatch')
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()


@method_decorator(cache_page(60 * 15), name='dispatch')
class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.prefetch_related('review_book').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = getattr(self.request, 'club', "Клуб не определен")
        return context
