from dataclasses import field
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email'),

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('__all__')




        
