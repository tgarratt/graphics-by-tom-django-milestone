from django.contrib import admin
from .models import purchase, purchase_line_item


class purchase_line_admin_in_line(admin.TabularInline):
    model = purchase_line_item


class purchase_admin(admin.ModelAdmin):
    inlines = (purchase_line_admin_in_line, )


admin.site.register(purchase, purchase_admin)
