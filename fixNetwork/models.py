from django.db import models

# Create your models here.

class FixNetwork(models.Model):
    router = models.CharField(max_length=200)
    m14 = models.CharField(max_length=200)
    m10 = models.CharField(max_length=200)

    def __str__(self):
        return self.router