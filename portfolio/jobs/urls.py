from django.urls import path 
from . import views

app_name = 'jobs'
urlpatterns = [
    path('jobExpenses/', views.index, name='jobs'),
    path('jobs/', views.JobsListView.as_view(), name='jobs_list'),
    path('jobsDetails/<uuid:pk>', views.JobsDetailView.as_view(), name='jobs_detail'),
    path('JobsCreate/', views.JobsCreateView.as_view(), name='jobs_create'),
    
]