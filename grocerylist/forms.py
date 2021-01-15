from django import forms
from .models import GroceryList

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = '__all__'