
from django.core.exceptions import ValidationError
from django import forms
from customers.models import *

from utils.django_forms import add_placeholder, strong_password

class CustomerRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Enter your username')
        add_placeholder(self.fields['name'], 'Enter your name')
        add_placeholder(self.fields['email'], 'Enter your email')
        add_placeholder(self.fields['phone'], 'Enter your phone number')
        add_placeholder(self.fields['password'], 'Enter your password')
    
    
    username = forms.CharField(
        error_messages={
            'required': 'Username'},
            label='Username'
    )    

    name = forms.CharField(
        error_messages={
            'required': 'Write your name'},
            label='Full Name'
    )
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',},
        label='Email Address',
        help_text='The e-mail must be valid.',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password is required'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[strong_password]
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirm Password',
        error_messages={
            'required': 'Password confirmation is required'
        }
    )

    class Meta:
        model = Customer
        fields = ['username', 'name', 'email', 'phone', 'password']
        
    
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if Customer.objects.filter(username=username).exists():
            raise ValidationError(
                'Username already exists', code='invalid'
            )
        return username
    

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if Customer.objects.filter(email=email).exists():
            raise ValidationError(
                'Email already exists', code='invalid'
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            self.add_error('password2', 'Passwords do not match')
        return cleaned_data
