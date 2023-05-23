from django.urls import path 
from . import views
app_name = 'budget'
urlpatterns = [
path('/', views.index, name='home'),
path('budget/', views.BudgetListView.as_view(), name='budget_list'),
path('budgetDetails/<uuid:pk>/', views.BudgetDetailView.as_view(), name=f'budget_detail'),
path('budgetCreate/', views.BudgetCreateView.as_view(), name='budget_create'),
path('budgetUpdate/<uuid:pk>/update', views.BudgetUpdateView.as_view(), name='budget_update'),
path('budgetDelete/<uuid:pk>/delete', views.BudgetDeleteView.as_view(), name='budget_delete'),
path('budget/budgetResults', views.SearchResultsList.as_view(), name='search'),

]
