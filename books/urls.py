from django.urls import path
from . import views


urlpatterns = [
    path('book_add/', views.add_book_view, name='book_add'),
    path('book_post_list/<int:id>/', views.book_detail_view),
    path('book_post_list/', views.book_list_view, name='book_post_list'),
    path('book_delete_list/', views.delete_book_view, name='book_delete_list'),
    path('book_post_list/<int:id>/delete/', views.book_drop_view),
    path('book_edit_list/', views.edit_book_view, name='book_edit_list'),
    path('book_edit_list/<int:id>/update/', views.update_view),

    path('info/', views.info_view),
    path('info_friend/', views.info_friend_view),
    path('time/', views.time_view),
]