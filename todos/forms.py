from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'id' : 'todo-list-item',
            'placeholder' : 'What will you do today?',
            'type' : 'text'
        }
    ))


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
