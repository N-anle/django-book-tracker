from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.sign_up, name = 'home'),
    path('login', views.login_view, name = 'login'),
    path('<str:username>/logout',views.logout_view, name = 'logout'),
    path('<str:username>/all_books' , views.all_books, name = 'all_books'),
    path('<str:username>/add_book',views.add_book, name = 'add_book'),
    path('edit_book/<int:book_id>', views.edit_book, name = 'edit_book'),
    path('<str:username>/delete_book/<int:book_id>', views.delete_book, name = 'delete_book'),
    path('search/<str:category>', views.category_search, name = 'category_search'),
    path('<str:username>/profile', views.user_profile, name = 'user_profile'),
    path('<int:book_id>/book_details', views.book_details, name = 'book_details'),
    path('<str:username>/edit_profile', views.edit_profile, name = 'edit_profile')
]