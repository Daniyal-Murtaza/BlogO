from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'tags', 'text')
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'}),
            'text': forms.Textarea(attrs={'rows': 10})
        }
