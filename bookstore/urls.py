from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', views.bookstore, name='bookstore'),
    path('search/', views.book_search, name='book-search'),
]