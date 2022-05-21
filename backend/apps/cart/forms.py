from django import forms



class CartAddForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class":"form-control"}
        )
    )
    update = forms.BooleanField(
        widget=forms.HiddenInput()
    )


