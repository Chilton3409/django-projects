from django.db import models
import datetime
import uuid
from django.urls import reverse
from django.db.models import Sum, Count, Max
from django.contrib import admin
from django.utils import timezone


# Create your models here.
class Bills(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    due_date = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now())
    description = models.TextField()

    
    class Meta:
        pass

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("bills:bills_detail", args=[str(self.id)])
    
    def get_total(self):
        total = Bills.objects.all().aggregate(Sum('amount')).pop('amount__sum')
        
        return total
        
            
      

       
        
        
        