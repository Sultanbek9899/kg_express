
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, 
    ListView,
    DetailView
)

import json
# Create your views here.
from .models import SubCategory, Category , Product, BanerImage

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baners = BanerImage.objects.all()
        if len(baners) > 6:
            baners = baners[:6]
        context['baners'] = baners
        return context

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 10
    #стандартное имя списка продуктов в шаблоне 
    # для ListView - object_list

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        if subcategory_slug: 
            products = Product.objects.filter(is_active=True, subcategory__slug=subcategory_slug)
        elif category_slug:
            products = Product.objects.filter(is_active=True, category__slug=category_slug)
        else:
            products = Product.objects.filter(is_active=True)
        return products  


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product" # стандартный object

