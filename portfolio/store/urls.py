from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('', views.index, name='home'),
   
    path('LeaveMessage/', views.BusinessCreateView.as_view(), name='business_create'),

    path('Contact/', views.BusinessListView.as_view(), name='business_list'),
    path('signup/', views.SignupAsView.as_view(), name='signup'),
    path('change_password/', views.change_password, name='change_password'),
    
    
    
]
