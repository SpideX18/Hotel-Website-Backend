from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250, db_index = True)     
    slug = models.SlugField(max_length=250, unique=True)
    cover_image = models.URLField(default='https://www.clipartmax.com/png/middle/141-1418392_overnight-services-bed-icon-png-blue.png')
    class Meta:
        verbose_name_plural = 'categories'    

    def __str__(self):
        return self.name


class Room(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=225)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.IntegerField()
    cover_image = models.URLField(default='https://www.clipartmax.com/png/middle/141-1418392_overnight-services-bed-icon-png-blue.png')
    recommended = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Rooms' 

    def __str__(self):
        return self.title
    

