from django import forms
from .models import add_piece


class add_piece_form(forms.ModelForm):
    class Meta:
        model = add_piece
        fields = (
            'title', 'company', 'piece_category', 'brief', 'use', 'where', 'piece')
