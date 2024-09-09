from django.urls import path
from . import views


urlpatterns = [
    path('book_post_list/<int:id>/', views.book_detail_view),
    path('book_post_list/', views.book_list_view),
    path('info/', views.info_view),
    path('info_friend/', views.info_friend_view),
    path('time/', views.time_view),
]