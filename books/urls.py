from django.urls import path
from . import views


urlpatterns = [
    path('info/', views.info_view),
    path('info_friend/', views.info_friend_view),
    path('time/', views.time_view),
]