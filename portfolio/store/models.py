from django.db import models
import uuid
from django.contrib import admin
from django.urls import reverse
from django.db.models import Sum, Count


# Create your models here.

    
    
    
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