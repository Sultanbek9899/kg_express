from itertools import product
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

from backend.apps.order.forms import OrderForm
class CartDetailView(View):

    def get(self, request):
        form = OrderForm()
        context = {"form":form}
        return render(self.request, "cart.html", context)


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

from django.http import JsonResponse

def add_cart_product(request,pk):
    if request.method == "POST":
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404
        cart = Cart(request)
        cart.add(
            product=product
        )
        return JsonResponse({"message":"Ok"}, status=200)
    return JsonResponse({"message":"Bad Request"}, status=400)


def minus_cart(request, pk):
    if request.method == "POST":
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404
        cart = Cart(request)
        cart.minus(
            product=product
        )
        return JsonResponse({"message":"Ok"}, status=200)
    return JsonResponse({"message":"Bad Request"}, status=400)