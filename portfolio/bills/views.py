from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Bills
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum



# Create your views here.

def index(request):
    num_bills = Bills.objects.all().count()
    total = Bills.objects.all().aggregate(Sum('amount'))

    context = {
        'num_bills': num_bills,
        'total': total
    }
    return render(request, 'bills/index.html', context=context)

class BillsListView(generic.ListView):
    model = Bills
    ordering = '-amount'
    context_object_name = 'bills'
    template_name = 'bills/bills_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["total"] = Bills.objects.all().aggregate(Sum('amount')).pop('amount__sum')
        return context



class BillsDetailView(generic.DetailView):
    model = Bills
    context_object_name = 'bills'
    template_name = 'bills/bills_detail.html'

class BillsCreateView(CreateView):
    model = Bills
    fields = ['name', 'amount', 'due_date', 'description']
    template_name = 'bills/bills_create.html'
    success_url = reverse_lazy("bills:bills_list")

class BillsUpdateView(UpdateView):
    model = Bills
    fields = ['name', 'amount', 'due_date', 'description']
    template_name = 'bills/bills_create.html'
    success_url = reverse_lazy("bills:bills_list")

class BillsDeleteView(DeleteView):
    model = Bills
    fields = ['name', 'amount', 'due_date', 'description']
    success_url = reverse_lazy("bills:bills_list")


    