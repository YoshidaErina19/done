from django import forms
from .models import Grocery


class GroceryCreateForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ('checkbox_1', 'checkbox_2', 'checkbox_3',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'