import django_filters
from django import forms

from backend.apps.product.models import Product

class ProductFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gt',
        label="Цена от",
        widget=forms.NumberInput(attrs={"class":"form-control"})
        
        )
    price__lt = django_filters.NumberFilter(
        field_name='price', 
        lookup_expr='lt',
        label="Цена до",
        widget=forms.NumberInput(attrs={"class":"form-control"})
        )
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    description = django_filters.CharFilter(
        field_name="description",
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )


    class Meta:
        model = Product
        fields = {
            'name',
            'description',
        }