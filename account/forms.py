from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, 
                                    AuthenticationForm, 
                                    UsernameField, 
                                    PasswordChangeForm,
                                    PasswordResetForm,
                                    SetPasswordForm)


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Confirm your password'}))
                                                            
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Enter your first name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Enter your last name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                            'placeholder': "Enter your email"}),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': "Enter your username"}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Password And Confirm Password Are Not Same! Please Enter The Same Password!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your username / email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }))
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Email'
        }))
        
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your new password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your new password'
            }))

class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label='Old Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your old password'
            }))

    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your new password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your new password'
            }))