from django.urls import path

from .views import *

urlpatterns = [
    path("category_list/", CategoryListApiView.as_view()),
    path("product_list/", ProductListApiView.as_view()),
    path('category/detail/<int:pk>/', CategoryDeitalApiView.as_view())
]