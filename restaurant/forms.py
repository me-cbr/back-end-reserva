from django import forms

from .models import User

class UserForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_field'}), label='Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input_field'}), label='Email')
    confirm_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input_field'}), label='Confirm Email')
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input_field'}), label='Phone')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_field'}), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_field'}), label='Confirm Password')
    
    class Meta:
        model = User
        fields = ['name', 'email', 'confirm_email' 'phone', 'password', 'confirm_password']
    
    def clean(self):
        cleanded_data = super().clean()
        
        password = cleanded_data.get('password')
        confirm_password = cleanded_data.get('confirmed_password')
        
        email = cleanded_data.get('email')
        confirm_email = cleanded_data.get('confirm_email')
        
        if password != confirm_password:
            raise forms.ValidationError('Password and Confirm Password do not match')
        
        if email != confirm_email:
            raise forms.ValidationError('Email and Confirm Email do not match')
        
        return cleanded_data

