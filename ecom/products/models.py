from django.db import models
from django.utils import timezone


class Product(models.Model):
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    category = models.CharField(max_length=200, default="General")
    availability = models.CharField(max_length=200, default="Available")
    pub_date = models.DateTimeField(timezone.now())
    product_img = models.FileField(upload_to="products/", max_length=255,null=True, default=None)

    def __str__(self):
        return self.title

