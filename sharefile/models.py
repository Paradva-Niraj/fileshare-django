from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NotesForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    photo = models.FileField(upload_to='', blank=True, null=True)

    def __str__(self):  
        return self.subject