from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
