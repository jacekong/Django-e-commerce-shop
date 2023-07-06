from django.urls import path,include
from tradeapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('all-products/', all_products, name='allproducts'),
    path('product-details/<str:slug>', ProductDetailView.as_view(), name='productdetails'),
    path('dashboard/', product_management, name='dashboard'),
    path('addproduct/', add_product, name='addproduct'),
    path('about/', about_us, name='about'),
    path('contact/', include('contact.urls')),
    path('update/<str:slug>', update_product, name='update'),
    path('products/category/<str:slug>', product_list, name='productlist'),
    path('search/', search, name='search'),
    path('add-category/', add_category, name='addcategory'),

]
