from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NotesForm(models.Model):
    subject = models.CharField(max_length=250)
    photo = models.FileField(upload_to='')

    def __str__(self):
        return self.file.name