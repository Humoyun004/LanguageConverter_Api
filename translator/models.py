from django.db import models


class TextTrans(models.Model):
    language_CHOICES = (
        ('latin', 'Latin'),
        ('cyrillic', 'Cyrillic'))
    context = models.TextField()
    pattern = models.CharField(max_length=20, choices=language_CHOICES)


class FileTrans(models.Model):
    language_CHOICES = (
        ('latin', 'latin'),
        ('cyrillic', 'cyrillic'))
    file = models.FileField(upload_to='file/', blank=True)
    pattern = models.CharField(max_length=20, choices=language_CHOICES)
