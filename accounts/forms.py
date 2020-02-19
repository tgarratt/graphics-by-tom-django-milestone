from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class sign_in_form(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class register_form(UserCreationForm):

    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password comfirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Account already exists with that email!')
        return email

    def clean_reg_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or password2:
            raise ValidationError("Please confirm your password!")

        if password1 != password2:
            raise ValidationError("Passwords must match!")

        return password2


