from django import forms

from models import UserDetail


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetail
        fields = ['username', 'password']
