from django import forms
from .models import NotesForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = NotesForm
        fields = ['subject', 'notefile', 'filetype']