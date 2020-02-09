from django.shortcuts import render
from order_work.models import order

# Create your views here.
def get_admin_orders(request):
    orders = order.objects.all()
    return render(request, "../templates/admin_orders.html", {"orders": orders})
