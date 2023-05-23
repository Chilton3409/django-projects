from django.db import models
import uuid 
from django.urls import reverse

# Create your models here.
class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)

    name = models.CharField(max_length=100)
    expenses = models.IntegerField()
    income = models.IntegerField()

    class Meta:
        pass
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse("budget:budget_detail", args=[str(self.id)])
    def get_total(self):
        total = self.income - self.expenses
        return total
    

    def after_tax(self):
        total = self.income - self.expenses
        after_tax = total - total * .10
        if after_tax > 0:
            return int(after_tax)
        else:
            message = "No taxable income"
            return message
    
    def savings(self):
        total = self.income - self.expenses
        savings =  int(total *.20)
        return savings
    
    def debt(self):
        total = self.income - self.expenses
        amount = total * .10
        if amount > 0:
            return round(amount)
        else: 
            message = "expenses exceed income"
            return message
        
    # calc percentage of expenses
    def totalpercent(self):
        total = self.expenses / self.income * 100
        newtotal = round(total)
        return newtotal