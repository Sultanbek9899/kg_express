from .models import Category,SubCategory



def get_categories(request):
    categories = Category.objects.all()
    return {"categories":categories}

