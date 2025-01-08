from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NotesForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=50)
    notefile = models.FileField(null=True,upload_to='media/')
    filetype = models.CharField(max_length=50)

    def __str__(self):  
        return self.subject