from django.db import models
from django.utils import timezone

# Create your models here.
class AppMessage(models.Model):
    text=models.TextField(default='Text')
    create_date=models.DateTimeField(
            default=timezone.now)
    read=models.BooleanField(default=False)

    def __str__(self):
        return self.text
