from backend.apps.cart.cart import Cart



def get_cart(request):
    cart = Cart(request)
    return {"cart":cart}

def get_register_form(request):
    form = UserregisterForm()
    return {"register_form":form}