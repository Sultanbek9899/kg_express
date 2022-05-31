from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('getSubcategory/', get_subcategory, name="get_subcategory"),
    path('list/product/', ProductListView.as_view(), name='product_list'),
    path('detail/product/<int:pk>/',ProductDetailView.as_view(), name="product_detail"),
    path('list/category/<slug:slug>/', ProductListView.as_view(), name="category_products"),
    path('list/category/<slug:slug>/<slug:subcategory_slug>/', ProductListView.as_view(), name="subcategory_products"),
    path('search/', ProductSearchView.as_view(), name="search")
]

# 'list/category/avtotovary/'
#'list/category/obuv/jenskaya/'