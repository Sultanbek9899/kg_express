from django.shortcuts import render


from django.views.generic import CreateView
# Create your views here.
from backend.apps.order.forms import OrderForm
from backend.apps.order.models import Order, OrderItem




class OrderCreatView(CreateView):
    form_class = OrderForm
    template_name = "order_create.html"
    
