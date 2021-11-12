from django import forms
from .models import Post, Author, Category


class PostForm(forms.ModelForm):
    id_author = forms.ModelChoiceField(label="Автор", queryset=Author.objects.all(), widget=forms.Select(attrs={"style": "width:100%"}))
    header = forms.CharField(label="Заголовок", widget=forms.TextInput(attrs={"style": "width:100%"}))
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"style": "width:100%"}))

    class Meta:
        model = Post
        fields = ['id_author', 'header', 'text']
