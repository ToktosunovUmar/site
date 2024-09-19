from django.urls import path
from . import views


urlpatterns = [
    path('book_add/', views.Addbookview.as_view(), name='book_add'),
    path('book_post_list/<int:id>/', views.Bookdetailview.as_view()),
    path('book_post_list/', views.Booklistview.as_view(), name='book_post_list'),
    path('book_delete_list/', views.Deletebookview.as_view(), name='book_delete_list'),
    path('book_post_list/<int:id>/delete/', views.Bookdropview.as_view()),
    path('book_edit_list/', views.Editbookview.as_view(), name='book_edit_list'),
    path('book_edit_list/<int:id>/update/', views.Updateview.as_view()),
    path('search/', views.Searchbookview.as_view(), name='search'),

    path('info/', views.info_view),
    path('info_friend/', views.info_friend_view),
    path('time/', views.time_view),
]