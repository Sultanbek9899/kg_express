from itertools import product
from django.shortcuts import render
from django.urls import reverse_lazy


from django.views.generic import CreateView
# Create your views here.
from backend.apps.order.forms import OrderForm
from backend.apps.order.models import Order, OrderItem
from backend.apps.cart.cart import Cart



class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = "order_create.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        order = form.save(commit=False)
        
        order.user = self.request.user
        order.save()
        cart = Cart(self.request)
        for item in cart:
            OrderItem.objects.create(
                product=item['product'],
                order=order,
                quantity=item['quantity'],
                price=item['price']
            )
        cart.clear()
        return super().form_valid(form)
        

