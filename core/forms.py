from django import forms 
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser


# create your forms here
class NewUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)
        