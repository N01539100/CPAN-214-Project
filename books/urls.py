from django.urls import path, include
from django.contrib.auth import views as auth_views

from books import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include('books.api.urls')),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]