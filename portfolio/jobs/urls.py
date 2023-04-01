from django.urls import path 
from . import views

app_name = 'jobs'
urlpatterns = [
    path('jobExpenses/', views.index, name='jobs'),
    path('jobs/', views.JobsListView.as_view(), name='jobs_list'),
    path('jobsDetails/<uuid:pk>/', views.JobsDetailView.as_view(), name='jobs_detail'),
    path('JobsCreate/', views.JobsCreateView.as_view(), name='jobs_create'),
    path('JobsUpdate/<uuid:pk>/update/', views.JobsUpdateView.as_view(), name='jobs_update'),
    path('jobsDelete/<uuid:pk>/delete/', views.JobsDeleteView.as_view(), name='jobs_delete'),
    path('expenses/', views.ExpenseListView.as_view(), name = 'expenses_list'),
    path('expensesDetail/<uuid:pk>/details/', views.ExpenseDetailView.as_view(), name='expenses_detail'),
    path('expenseCreate/', views.ExpenseCreateView.as_view(), name='expenses_create'),
    path('expenseUpdate/<uuid:pk>/update', views.ExpenseUpdateView.as_view(), name='expenses_update'),
    path('expenseDelete/<uuid:pk>/delete', views.ExpenseDeleteView.as_view(), name='expenses_delete'),
    path('incomeCreate/', views.IncomeCreateView.as_view(), name="income_create"),

    
]