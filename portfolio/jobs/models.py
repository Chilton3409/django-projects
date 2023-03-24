from django.db import models
import uuid
from django.contrib import admin
from django.urls import reverse
from django.db.models import Sum

# Create your models here.
class Expenses(models.Model):
    


    EXPENSE_TYPE = (
        ('a', 'Advertising'),
        ('f', 'Fees'),
        ('m', 'Misc'),
        ('w', 'Wages'),
        ('u', 'Utilities'),

    )
    expenses = models.CharField(max_length=1, choices=EXPENSE_TYPE, blank=True, null=False, help_text="Choose business expense type")
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    class Meta:
        pass
    def __str__(self):
        return f'{self.amount}'

   

    def get_absolute_url(self):
        pass
    
class Mileage(models.Model):
    #need business miles and personal miles
    #then divide total miles by business miles to get business percentage
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
    personal = models.IntegerField(help_text="Enter personal use miles")
    business = models.IntegerField(help_text="Enter business use miles")
    
    def get_miles(self):
     
        total = int(self.business + self.personal)

        return total    
    def business_miles(self):
        total_miles = int(self.business + self.personal)
        business_miles = total_miles * .62
        return business_miles

    def __str__(self):
        return f'{self.business}'

    

class Jobs(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
    job_name = models.CharField(max_length=200, null=False, blank=True, help_text="Enter name for job you are tracking")
    client = models.CharField(max_length=100, null=False, blank=True, help_text="Enter clients name")
    date = models.DateTimeField(auto_now_add=False)
    expenses = models.ManyToManyField(Expenses)
    mileage = models.ForeignKey(Mileage,primary_key=False ,on_delete=models.DO_NOTHING, default=0, blank=True, null=True)
    
    #ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))
# returns {'field_name__sum': 1000} for example

    class Meta:
        ordering = ['client']

    def get_total(self):
        total = (self.expenses.aggregate(Sum('amount')))
        return total.pop('amount__sum')
    
   

    
        
        
    def __str__(self):
        return f'{self.client}'
    
    def get_absolute_url(self):
        return reverse("jobs:jobs_detail", args=[str(self.id)])
    
   
    

    

