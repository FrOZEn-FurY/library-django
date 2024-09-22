from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BookForm
from.models import Book
from django.contrib import messages


class ShowBooks(ListView):
    template_name = 'book/showBooks.html'
    model = Book
    context_object_name = 'books'


class AddBook(CreateView):
    template_name = 'book/bookForm.html'
    form_class = BookForm
    model = Book
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Book added successfully!')
        return super().form_valid(form)


class EditBook(UpdateView):
    template_name = 'book/bookForm.html'
    form_class = BookForm
    model = Book
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)


class DeleteBook(DeleteView):
    model = Book
    success_url = '/'