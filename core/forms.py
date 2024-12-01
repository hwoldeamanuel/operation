from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField


from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            msg = 'A user with that email already exists.'
            self.add_error('email', msg)           
    
        return self.cleaned_data
       


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)
        

class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Ah, ah, ah. You didn't say the magic word!",
        "inactive": "Permission denied",
    }

class BasicUserDataForm(forms.Form):
  error_css_class = 'is-invalid'
  user_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})) 

  class Meta:
    model = User   