from django.contrib import admin
from .models import Business
# Register your models here.




class BusinessAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Business, BusinessAdmin)
