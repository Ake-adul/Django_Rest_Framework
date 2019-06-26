from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField()

    def __str__(self):
        return self.name