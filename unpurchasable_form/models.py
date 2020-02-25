from django.db import models


class add_piece(models.Model):

    title = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=50, blank=False, default='')
    brief = models.CharField(max_length=200, blank=False, default='')
    PIECE_CATEGORY_CHOICES = (
        ('25', 'Logo'), ('20', 'Clothing'), ('30', 'WebApp'),
        ('35', 'Advertising'), ('40', 'Illistration'),
        ('15', 'Packaging'))
    piece_category = models.CharField(
        max_length=50, choices=PIECE_CATEGORY_CHOICES, default='')
    use = models.CharField(max_length=50, blank=False, default='')
    where = models.URLField(max_length=100, blank=False, default='')
    piece = models.ImageField(upload_to="piece_img", blank=True, null=True)

    def __str__(self):
        return self.title

