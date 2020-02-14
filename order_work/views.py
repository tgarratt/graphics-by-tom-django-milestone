from django.shortcuts import render, HttpResponse
from .forms import order_form


def get_order_work(request):
    if request.method == "POST":
        print(request.POST)
        form_order = order_form(request.POST, request.FILES)
        if form_order.is_valid():
            the_order = form_order.save()
            total = int(request.POST.get('category')) + int(request.POST.get('when'))
            the_order.order_total = total
            the_order.save()
            print("Success")

    else:
        form_order = order_form()

    return render(
        request, "../templates/order_work.html", {"form": form_order})
