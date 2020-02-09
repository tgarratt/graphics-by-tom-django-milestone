from django.db import models
from django.utils import timezone
from django import forms

class order(models.Model):

    title = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=50, blank=False, default='')
    brief = models.CharField(max_length=200, blank=False, default='')
    CATEGORY_CHOICES = (('Logo', 'Logo'), ('Clothing', 'Clothing'), ('WebApp', 'WebApp'), ('Advertising', 'Advertising'), ('Illistration', 'Illistration'), ('Packaging', 'Packaging'))
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='')
    use = models.CharField(max_length=50, blank=False, default='')
    WHEN_CHOICES = (('ASAP', 'ASAP',), ('1 week', '1 Week'), ('2 weeks', '2 Weeks'), ('4 weeks+', '4 weeks+'))
    when = models.CharField(max_length=50, choices=WHEN_CHOICES, default='')
    inspiration = models.URLField(max_length=100, blank=False, default='')
    draft = models.ImageField(upload_to="img/draft", blank=True, null=True)

    def __str__(self):
        return self.title

