from django.shortcuts import render, get_object_or_404, redirect, reverse
from order_work.models import order


def get_admin_orders(request):
    # displays all of the paid for orders 
    orders = order.objects.filter(paid=True)
    return render(request, "../templates/admin_orders.html", {"orders": orders})


def get_admin_orders_delete(request, pk=None):
    # method to delete the orders when they are complete 
    delete_order = get_object_or_404(order, pk=pk)
    delete_order.delete()

    return redirect(reverse('admin_orders'))