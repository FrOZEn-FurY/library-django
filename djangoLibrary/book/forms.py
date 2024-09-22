from .models import Book
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_at', 'updated_at']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20,
                                                 "class": "textarea textarea-info",
                                                 "style": "width: 100%; resize: none;"}),
            'image': forms.FileInput(attrs={"class": "file-input file-input-bordered file-input-info w-full max-w-xs"}),
            'author': forms.TextInput(attrs={"class": "input input-bordered input-info w-full max-w-xs"}),
            'title': forms.TextInput(attrs={"class": "input input-bordered input-info w-full max-w-xs"}),
        }