from django.db import models
import uuid
from django.contrib import admin
from django.urls import reverse
from django.db.models import Sum, Count


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Enter product name")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    price = models.IntegerField()
    inv = models.IntegerField(null=True, blank=True, help_text="Enter current inventory")
    description = models.TextField(null=True, blank=True, help_text="Enter a description of your products")

    class Meta:
        pass

    def __str__(self):
        return f'{self.name} {self.inv}'
    
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[str(self.id)])
    


class Store(models.Model):
    headline = models.CharField(max_length=100, null=True, blank=True)
    Items = models.ManyToManyField(Product)


    class Meta:
        pass

    def __str__(self):
        return f'{self.headline}'
    
    def count_products(self):
        count = self.Items.aggregate(Sum('inv'))
      
        return count
    
    def get_absolute_url(self):
        return reverse("store:store_detail", args=[str(self.id)])
    
    
    
class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)

    email = models.EmailField(primary_key=False, help_text="Enter business email")
    phone = models.IntegerField(max_length=12, null=False, blank=False, help_text="Enter business phone number")
    message = models.TextField(null=True, blank=True, help_text='leave a brief message for clients')
    class Meta:
        ordering = ['email']

    def __str__(self):
        return f'{self.email}'
    
    def get_absolute_url(self):
        pass