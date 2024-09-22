from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.ShowBooks.as_view(), name='showBooks'),
    path('addBook/', views.AddBook.as_view(), name='addBook'),
    path('editBook/<int:pk>', views.EditBook.as_view(), name='editBook'),
    path('deleteBook/<int:pk>', views.DeleteBook.as_view(), name='deleteBook'),
]