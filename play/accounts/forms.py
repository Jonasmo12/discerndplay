from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from django.contrib.auth.models import (
    User
)
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if User.objects.filter(username=username).exists():
            raise ValidationError('username in use')

        if User.objects.filter(email=email).exists():
            raise ValidationError('email has been taken')
        
        return self.cleaned_data
