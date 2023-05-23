from django.shortcuts import render
from django.conf import settings 
from django.shortcuts import render
from .models import Business
from django.views import generic 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db.models import Avg, Count, Min, Max, Sum
from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth import get_user_model
from users.forms import CustomUserCreationForm, CustomUserChangeForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView







import os



# Create your views here.z
def index(request):
    num_products = Business.objects.all().count()

    context = {
        'num_products': num_products,
    }

    return render(request, 'store/index.html', context=context)



class BusinessListView(generic.ListView):
    model = Business
    context_object_name = 'business_list'
    template_name='store/business_list.html'

class BusinessCreateView(CreateView):
    model = Business
    fields = ['email', 'phone', 'message']
    template_name = 'store/business_create.html'
    success_url = reverse_lazy('store:home')


class SignupAsView(CreateView):
   
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
   
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })