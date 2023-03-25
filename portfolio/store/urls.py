from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.ProductListView.as_view(), name='product_list'),
    path('productInfo/<uuid:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('productCreate/', views.ProductCreateView.as_view(), name='product_create'),
    path('productUpdate/<uuid:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<uuid:pk>/delete', views.ProductDeleteView.as_view(), name='product_delete'),

    path('store/', views.StoreListView.as_view(), name='store_list'),
    path('storeDetail/<int:pk>/', views.StoreDetailView.as_view(), name='store_detail'),
    path('storeCreate/', views.StoreCreateView.as_view(), name='store_create'),
    path('storeUpdate/<int:pk>/update', views.StoreUpdateView.as_view(), name='store_update'),
    path('storeDelete/<int:pk>/delete', views.StoreDeleteView.as_view(), name='store_delete'),
    path('Contact/', views.BusinessListView.as_view(), name='business_list'),
    path('signup/', views.SignupAsView.as_view(), name='signup'),
    path('change_password/', views.change_password, name='change_password'),
    
    
    
]
