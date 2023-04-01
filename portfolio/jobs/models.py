from django.db import models
import uuid
from django.contrib import admin
from django.urls import reverse
from django.db.models import Sum
from django.utils import timezone

# Create your models here.
class Expenses(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)

    EXPENSE_TYPE = (
        ('a', 'Advertising'),
        ('f', 'Fees'),
        ('m', 'Misc'),
        ('w', 'Wages'),
        ('u', 'Utilities'),

    )
    expenses = models.CharField(max_length=1, choices=EXPENSE_TYPE, blank=True, null=False, help_text="Choose business expense type")
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    class Meta:
        pass
    def __str__(self):
        return f'{self.amount}'
    def get_absolute_url(self):
        return reverse("jobs:expenses_detail", args=[str(self.id)])
    
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

#going to write an income model to depict income coming in
#then write many to many in the jobs model to track income coming in and compare it against expenses
class Income(models.Model):
        id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
        date = models.DateTimeField(auto_now_add=True)
        amount = models.IntegerField(null=False, blank=True, default=0, help_text="Enter amount earned")

        class Meta:
            ordering = ['amount']

        def __str__(self):
            return f'{self.amount}'
        

class Jobs(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
    job_name = models.CharField(max_length=200, null=False, blank=True, help_text="Enter name for job you are tracking")
    client = models.CharField(max_length=100, null=False, blank=True, help_text="Enter clients name")
    date = models.DateTimeField(auto_now_add=True)
    income = models.ManyToManyField(Income)
    expenses = models.ManyToManyField(Expenses, default=0)
    mileage = models.ForeignKey(Mileage,primary_key=False ,on_delete=models.DO_NOTHING, default=0, blank=True, null=True)
    
    #ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))
# returns {'field_name__sum': 1000} for example

    class Meta:
        ordering = ['client']

    def get_total(self):
        total = (self.expenses.aggregate(Sum('amount')))
        return total.pop('amount__sum')
    
    def get_wages(self):
        income = (self.income.aggregate(Sum('amount')))
        return income.pop('amount__sum')

    def get_profit(self):
        if self.expenses is not TypeError:
            income = (self.income.aggregate(Sum('amount'))).pop('amount__sum')
            total = (self.expenses.aggregate(Sum('amount'))).pop('amount__sum')
            if total is None:
                total = 0
            return int(income - total)
        else:
            return('cant')

       


         
   

        

       
        

    def __str__(self):
        return f'{self.client}'
    
    def get_absolute_url(self):
        return reverse("jobs:jobs_detail", args=[str(self.id)])
    
   
    

    

