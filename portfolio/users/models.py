from email.policy import default
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
from django.db.models import Sum
from django.db.models.functions import Coalesce





from .managers import CustomUserManager #manager class we created in managers.py




# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

#create a simple model for my hemp store
class Lotion(models.Model):
    #going to add sparse model idea here
    # a way to tell if order is virtual or physical (aka in person)
    # I live for this shit.
   
    #end sparse model
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text="In cents")
    #specific attrubutes

    dosage = models.PositiveIntegerField(help_text='in milligrams')
    download_link = models.URLField(null=True, blank=True,)

    

    #going to add JSON
    extra = JSONField(default=dict)

    def __str__(self):
        return f'{self.name}'
        
   

#moving to Abstract Base Classes

class Product(models.Model):
    class Meta:
        abstract=True

    TYPE_PHYSICAL = 'physical'
    TYPE_VIRTUAL = 'virtual'
    TYPE_CHOICES = (
        (TYPE_PHYSICAL, 'Physical'),
        (TYPE_VIRTUAL, 'Virtual'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_PHYSICAL, help_text='Choose how you would like to place your order.')


    
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text='in cents')
    
    def __str__(self) -> str:
        return f'[{[{self.get_type_display()}]}]{self.name}'
    
    def clean(self) -> None:
        if self.type == Lotion.TYPE_VIRTUAL:
            if self.dosage == 0:
                raise ValidationError('A virtual product dosage cannot equal 0')
        if self.download_link is None:
            raise ValidationError('A virtual Product must have a download link')

        else: 
            assert False, f'Unknown shit is going down with "{self.type}"'

class Tincture(Product):
    dose = models.PositiveIntegerField(help_text='in milligrams')

class OnlineTincture(Product):
    download_link = models.URLField()

class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), primary_key=True,on_delete=models.CASCADE)

    lotion = models.ManyToManyField(Lotion)
    tincture = models.ManyToManyField(Tincture)
   
    def __str__(self):
        return str(self.user)

    def clean(self) -> None:
        if self.user == ObjectDoesNotExist:
            raise ObjectDoesNotExist('error')

    def get_total(self):
        pass


#models associated with the permissions tutorial

        

   
    #set a custom permission called set_published_status
    """
    in order to enforce the below permission, use UserPassesTestMixin in the view, giving us
    the flexibility to explicitly check whether  user has the required permission or not

    """


    