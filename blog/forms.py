from django import forms
from .models import Post


class PostForm(forms.Form):

    p_title = forms.CharField(label="Título", max_length=100)
    p_topic = forms.CharField(label="Tema", max_length=200)
    p_content = forms.CharField(label="Contenido", widget=forms.Textarea)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'topic', 'content')

