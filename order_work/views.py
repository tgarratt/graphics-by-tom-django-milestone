from django.shortcuts import render, HttpResponse
from .forms import order_form


def get_order_work(request):
    if request.method == "POST":
        form_order = order_form(request.POST, request.FILES)
        if form_order.is_valid():
            form_order.save()
            print("Success")

    else:
        form_order = order_form()

    return render(
        request, "../templates/order_work.html", {"form": form_order})
