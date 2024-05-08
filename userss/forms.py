from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
User=get_user_model()

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model=User
  


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    first_name = forms.CharField()
    last_name= forms.CharField()
    email= forms.CharField()
    class Meta:
        model=User
        fields=(
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

class ProfileForm(UserChangeForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name= forms.CharField()
    email= forms.CharField()
    address= forms.CharField()
    class Meta:
        model=User
        fields=(
            "username",
            "first_name",
            "last_name",
            "address",
            "email",
        )
    
    