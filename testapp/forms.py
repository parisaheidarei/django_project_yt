from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(label='title' , max_length=200)
    content = forms.CharField(label='content' , widget=forms.Textarea)

    image = forms.ImageField()