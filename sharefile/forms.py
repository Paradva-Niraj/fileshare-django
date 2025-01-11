from django import forms
from .models import NotesForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NotesForm(forms.ModelForm):
    class Meta:
        model = NotesForm
        fields =['user','subject','photo']

class userregistrationform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
