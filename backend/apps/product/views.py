import imp
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from .models import SubCategory

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
