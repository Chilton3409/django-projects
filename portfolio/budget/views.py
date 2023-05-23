from django.shortcuts import render
from .models import Budget
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum

from django.db.models import Q



# Create your views here.

def index(request):
    num_bud = Budget.objects.all().count

    context = {
        'num_bud': num_bud
    }

    return render(request, 'budget/index.html', context=context)

class BudgetListView(generic.ListView):
    model = Budget
    context_object_name = 'budget'
    template_name = 'budget/budget_list.html'

    def get_context_data(self, **kwargs):
        #call base
        context = super().get_context_data(**kwargs)
        #add custom query to pass in
        income = Budget.objects.all().aggregate(Sum('income')).pop('income__sum')
        expenses = Budget.objects.all().aggregate(Sum('expenses')).pop('expenses__sum')

        if income is not None:
            total = income - expenses
            context["overall_total"] = total
            return context
class BudgetDetailView(generic.DetailView):
    model = Budget
    context_object_name = 'budget'
    template_name = 'budget/budget_detail.html'
    
class BudgetCreateView(CreateView):
    model = Budget
    fields = ['name', 'income', 'expenses']
    success_url = reverse_lazy('budget:budget_list')
    template_name = 'budget/budget_create.html'

class BudgetUpdateView(UpdateView):
    model = Budget
    fields = ['name', 'income', 'expenses']
    template_name = 'budget/budget_create.html'
    success_url = reverse_lazy('budget:budget_list')

class BudgetDeleteView(DeleteView):
    model = Budget
    fields = ['name', 'income', 'expenses']
    success_url = reverse_lazy('budget:budget_list')

class SearchResultsList(generic.ListView):
    model = Budget
    context_object_name = 'budget'
    template_name = 'budget/budget_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query != '':
            return Budget.objects.filter(name__icontains=query)
        