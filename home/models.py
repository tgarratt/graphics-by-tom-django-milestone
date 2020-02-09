from django.db import models

# Create your models here.
class Design(models.Model):
    title = models.CharField(max_length=30, blank=False)
    brief = models.CharField(max_length=100, blank=False, default='')
    purchasable = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.title

