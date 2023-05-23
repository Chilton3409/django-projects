from django.urls import path 
from . import views

app_name = 'bills'

urlpatterns = [
    path('/', views.index, name='home'),
    path('bills/', views.BillsListView.as_view(), name='bills_list'),
    path('billDetail/<uuid:pk>/', views.BillsDetailView.as_view(), name='bills_detail'),
    path('billsCreate/', views.BillsCreateView.as_view(), name='bills_create'),
    path('billsUpdate/<uuid:pk>/update', views.BillsUpdateView.as_view(), name='bills_update'),
    path('billsDelete/<uuid:pk>/delete', views.BillsDeleteView.as_view(), name='bills_delete'),
    
]