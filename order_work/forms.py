from django import forms
from .models import order


class order_form(forms.ModelForm):
    class Meta:
        model = order
        fields = (
            'title', 'company', 'category', 'brief',
            'use', 'when', 'inspiration', 'draft')


