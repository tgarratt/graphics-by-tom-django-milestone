from django.db import models
from order_work.models import order


class purchase(models.Model):
    full_name_or_company = models.CharField(max_length=50, blank=False)
    Email = models.CharField(max_length=50, blank=False)
    contact_number = models.CharField(max_length=20, blank=False)
    request_date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(self.id, self.full_name_or_company)


class purchase_line_item(models.Model):
    buy = models.ForeignKey(purchase, null=False)
    work = models.ForeignKey(order, null=False)

    def __str__(self):
        return "{0}-{1}".format(self.order.order_total, self.order.title)
        
