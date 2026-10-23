from django import forms  # type: ignore
from .models import GroceryItem


class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = [
            "name",
            "category",
            "quantity",
            "unit",
            "date_purchased",
            "expiration_date",
            "notes",
        ]
        widgets = {
            "date_purchased": forms.DateInput(attrs={"type": "date"}),
            "expiration_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }