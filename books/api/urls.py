from django.urls import path

from books.api import views

urlpatterns = [
    path('', views.getRoutes),
    path('books/', views.getBooks, name='api_books'),
    path('books/<int:pk>/', views.getBook, name='api_book'),
]
