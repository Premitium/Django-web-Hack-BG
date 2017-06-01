from django.contrib.auth.models import User
from django import forms
from .models import BlogPost


class LoginForm(forms.Form):
    use_required_attribute = False

    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)

class BlogPostCreateModelForm(forms.ModelForm):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['tags'].required = False

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'tags', 'is_private')


class BlogPostCreateForm(forms.Form):
    use_required_attribute = False

    title = forms.CharField(label='Title', max_length=255)
    content = forms.CharField(widget=forms.Textarea)

class BlogPostRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
