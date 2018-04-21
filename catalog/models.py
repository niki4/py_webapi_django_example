import os
from django.db import models
from django.core.files.storage import FileSystemStorage

media_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media/catalog/images/')
fs = FileSystemStorage(location=media_path)


class Product(models.Model):
    title = models.CharField(max_length=200)
    price_rub = models.IntegerField('Price in rubles')
    product_image = models.FileField(storage=fs)
    in_store = models.BooleanField(default=False)

    departments = models.ManyToManyField('Department', related_name='products')
    features = models.ManyToManyField('Feature', blank=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
