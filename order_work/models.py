from django.db import models


class order(models.Model):

    title = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=50, blank=False, default='')
    brief = models.CharField(max_length=200, blank=False, default='')
    CATEGORY_CHOICES = (
        ('25', 'Logo'), ('20', 'Clothing'), ('30', 'WebApp'),
        ('35', 'Advertising'), ('40', 'Illistration'),
        ('15', 'Packaging'))
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='')
    use = models.CharField(max_length=50, blank=False, default='')
    WHEN_CHOICES = (
        ('50', 'ASAP',), ('40', '1 Week'), ('30', '2 Weeks'), ('20', '4 weeks+'))
    when = models.CharField(max_length=50, choices=WHEN_CHOICES, default='')
    inspiration = models.URLField(max_length=100, blank=False, default='')
    draft = models.ImageField(upload_to="media/draft_img", blank=True, null=True)
    order_total = models.IntegerField(default=0)

    def __str__(self):
        return self.title

