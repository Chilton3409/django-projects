from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.ProductListView.as_view(), name='product_list'),
    path('productInfo/<uuid:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('store/', views.StoreListView.as_view(), name='store_list'),
    path('storeDetail/<int:pk>/', views.StoreDetailView.as_view(), name='store_detail'),
    path('Contact/', views.BusinessListView.as_view(), name='business_list'),
    path('signup/', views.SignupAsView.as_view(), name='signup'),
    path('change_password/', views.change_password, name='change_password'),
    
    
    
]
