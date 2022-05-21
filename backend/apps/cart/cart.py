
from decimal import Decimal
from django.conf import settings
from backend.apps.product.models import Product

class Cart(): 

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product,  quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity":0, "price":str(product.price)}
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values:
            item['price'] = Decimal(item['price']) #превращаем в Decimal
            item['total_price'] = item['price'] * item['quantity']
            yield item        

    def __len__(self):
        return (item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        product_total = []
        for item in self.cart.values():
            product_total.append(Decimal(item['price']) * item['quantity'])
        return sum(product_total)
    
    def clear(self):
        # очищает корзину
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True

