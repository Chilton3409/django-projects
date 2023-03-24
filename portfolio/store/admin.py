from django.contrib import admin
from .models import Store, Product, Business
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Product, ProductAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ['headline']

admin.site.register(Store, StoreAdmin)

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Business, BusinessAdmin)
