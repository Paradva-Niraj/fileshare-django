# Generated by Django 5.1.4 on 2025-01-11 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharefile', '0005_alter_notesform_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesform',
            name='user',
        ),
    ]
