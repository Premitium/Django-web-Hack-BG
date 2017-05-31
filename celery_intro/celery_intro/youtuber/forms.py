from django import forms

class SubmitForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    url = forms.URLField(label="Link to song")
