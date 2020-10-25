from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from material import Layout, Row, Fieldset
# from protect.config import *
import logging

log = logging.getLogger(__name__)
# convert the errors to text
from django.utils.encoding import force_text



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text= 'Required. Add a valid email address')
    
    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    layout = Layout(
                    Fieldset('Account details',
                              'username', 'email',
                    Row('password1', 'password2') ),
                    Fieldset('Personal details',
                             Row('first_name', 'last_name')) )

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    layout = Layout(
        Fieldset('Please Log In',
                 'email', 'password'))

    def clean(self):
        if self.is_valid():
         email = self.cleaned_data['email']
         password = self.cleaned_data['password']
         if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")