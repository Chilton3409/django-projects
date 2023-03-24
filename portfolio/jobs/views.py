from django.shortcuts import render
from .models import Jobs, Expenses
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Create your views here.
def index(request):
    num_jobs = Jobs.objects.all().count()

    context = {
        'num_jobs': num_jobs,

    }
    return render(request, 'jobs/index.html', context=context)

class JobsListView(generic.ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = 'jobs/jobs_list.html'

class JobsDetailView(generic.DetailView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = 'jobs/jobs_detail.html'

class JobsCreateView(CreateView):
    model = Jobs 
    fields = ['client', 'date', 'expenses', 'mileage']
    success_url = reverse_lazy('jobs:jobs_list')
    template_name = 'jobs/jobs_create.html'

class ExpenseCreateView(CreateView):
    model = Expenses
    pass