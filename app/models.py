from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
    highlighted = models.TextField()
