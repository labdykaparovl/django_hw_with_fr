from django.db import models

class Courier(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
