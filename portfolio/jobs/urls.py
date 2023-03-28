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
    path('expenseCreate/', views.ExpenseCreateView.as_view(), name='expense_create'),
    path('incomeCreate/', views.IncomeCreateView.as_view(), name="income_create"),

    
]