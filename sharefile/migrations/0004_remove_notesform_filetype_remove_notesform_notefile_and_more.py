# Generated by Django 5.1.4 on 2025-01-11 08:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharefile', '0003_alter_notesform_notefile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesform',
            name='filetype',
        ),
        migrations.RemoveField(
            model_name='notesform',
            name='notefile',
        ),
        migrations.AddField(
            model_name='notesform',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='notesform',
            name='subject',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='notesform',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]