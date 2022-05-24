from backend.apps.cart.cart import Cart


def get_cart(request):
    cart = Cart(request)
    # for i in cart:
    #     print(i)
    return {"cart":cart}
