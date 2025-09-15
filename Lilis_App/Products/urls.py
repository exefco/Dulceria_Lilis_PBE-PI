from django.urls import path
from .views import Dashboard, Products_view

urlpatterns = [
    path('dashboard/', Dashboard.as_view(template_name='products/dashboard.html'), name='products_dashboard'),
    path('products/', Products_view.as_view(template_name='products/products.html'), name='products'),

]