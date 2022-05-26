from django import forms

from backend.apps.order.models import Order




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'address',
            'postal_code',
            'mobile',
            "notice"
        ]
        widgets = {
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "postal_code":forms.TextInput(attrs={"class":"form-control"}),
            "mobile":forms.TextInput(attrs={"class":"form-control"}),
            "notice":forms.TextInput(attrs={"class":"form-control"}),
        }
