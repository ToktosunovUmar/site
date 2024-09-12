from django.urls import path
from . import views

urlpatterns = [
    path('for_kids/', views.filter_view),
    path('for_adult/', views.filter_view),
    path('for_kids/', views.filter_view),
]