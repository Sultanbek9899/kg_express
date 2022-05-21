from django.shortcuts import render, redirect

from django.views import View
from django.http import Http404
# Create your views here.

from .forms import CartAddForm
from .cart import Cart
from backend.apps.product.models import Product

class AddCartView(View):


    def get(self, request, pk):
        product_id = self.kwargs.get('pk')
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        cart.add(
            product=product, 
        )
        return redirect("cart_detail")


class CartDetailView(View):

    def get(self, request):
        return render(self.request, "cart.html")


class RemoveCartView(View):

    def get(self,request,pk):
        cart = Cart(request)
        try:
            product=Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404
        cart.remove(product)
        return redirect('cart_detail')

class ClearCartView(View):

    def get(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect('cart_detail')
