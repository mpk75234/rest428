from django.db import models

class Verbos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    verb = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    class Meta:
        ordering = ('created',)