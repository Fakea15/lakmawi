from django import forms
from .models import Post, Message

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description', 'author')
        labels = {
            'title': 'Thlalak zawn awl nan',
            'image': 'I thlalak duh thlang rawh ',
            'description': 'He thlalak chungchang'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: pangpar sen'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        labels = {
            'sender': '',
            'email': '',
            'message': ''
        }

        widgets = {
            'sender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hming'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'I message chu lo ziak tan rawh le!'})
        }


