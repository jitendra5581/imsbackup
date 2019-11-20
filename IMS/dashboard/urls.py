
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index,name='dashboard_home'),
    path('purchase', purchase_view,name='purchase'),
    path('measures', measures_view,name='measures'),
    path('product',product_view,name='product'),
    path('invproduct', inventory_product_view,name='invproduct'),
    path('', index,name='dashboard_home'),
    path('', index,name='dashboard_home'),
    path('', index,name='dashboard_home'),



]
