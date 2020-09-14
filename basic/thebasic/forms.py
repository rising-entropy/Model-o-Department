from django.contrib.auth.models import User
from django import forms


# Model class gives us blueprint for our own form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


