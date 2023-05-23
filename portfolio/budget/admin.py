from django.contrib import admin
from .models import Budget

# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Budget, BudgetAdmin)