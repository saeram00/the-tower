from django import forms


class PostForm(forms.Form):

    p_title = forms.CharField(max_length=100)
    p_topic = forms.Charfield(max_length=200)
    p_content = forms.CharField(widget=forms.Textarea)

