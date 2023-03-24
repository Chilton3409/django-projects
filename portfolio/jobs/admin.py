from django.contrib import admin
from .models import Expenses, Jobs, Mileage

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['expenses']

admin.site.register(Expenses, ExpenseAdmin)

class JobsAdmin(admin.ModelAdmin):
    list_display = ['client']

admin.site.register(Jobs, JobsAdmin)

class MileageAdmin(admin.ModelAdmin):
    list_display = ['personal']

admin.site.register(Mileage, MileageAdmin)

