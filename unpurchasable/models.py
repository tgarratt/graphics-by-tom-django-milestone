from django.db import models


class filter_piece(models.Model): 
    PIECE_FILTER_CHOICES = (
        ('25', 'Logo'), ('20', 'Clothing'), ('30', 'WebApp'),
        ('35', 'Advertising'), ('40', 'Illistration'),
        ('15', 'Packaging'))
    piece_filter = models.CharField(
        max_length=50, choices=PIECE_FILTER_CHOICES, default='')
