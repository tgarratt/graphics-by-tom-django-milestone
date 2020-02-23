from django import forms
from .models import filter_piece


class filter_piece_form(forms.ModelForm):
    class Meta:
        model = filter_piece
        fields = ('__all__')
        