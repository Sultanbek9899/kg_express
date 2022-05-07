
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
from .models import SubCategory, Category , Product

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(TemplateView):
    template_name = "index.html"



class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
    queryset = Product.objects.filter(is_active=True)
    #стандартное имя списка продуктов в шаблоне 
    # для ListView - object_list



class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product" # стандартный object
    # 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs'] = SubCategory.objects.all()
        print(context)
        return context
