from django.urls import path

from .views import * 

urlpatterns = [
    path(
        'create/', 
        OrderCreateView.as_view(),
        name="order_create"
        )
]