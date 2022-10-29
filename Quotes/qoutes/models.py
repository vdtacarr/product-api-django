from django.db import models


# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=50)

    likes = models.PositiveIntegerField(default=0)

    def __dir__(self):
        return self.title

class Product(models.Model):
    price = models.FloatField(null=True)
    description = models.TextField(null=True)
    now = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.description
