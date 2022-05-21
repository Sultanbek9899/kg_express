from django.urls import path

from .views import *

urlpatterns = [
    path('', CartDetailView.as_view(),name="cart_detail"),
    path('add/<int:pk>/',AddCartView.as_view(), name="add_cart"),
]