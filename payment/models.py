from django.db import models


class customer_info (models.Model):

    customer_username = models.CharField(max_length=50, blank=False, default='')
    customer_email = models.CharField(max_length=50, blank=False, default='')
    customer_number = models.IntegerField(blank=False, default='')

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.customer_username, self.customer_email, self.customer_number)

