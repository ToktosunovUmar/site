from django.urls import path
from . import views

urlpatterns = [
    path('rezka_films_list/', views.RezkaFilListView.as_view(), name='rezka_film_list'),
    path('start_parser/', views.ParserFormView.as_view()),
]