from django.shortcuts import render, redirect, reverse
from .forms import order_form
from django.contrib.auth.decorators import login_required


@login_required()
def get_order_work(request):
    if request.method == "POST":
        print(request.POST)
        form_order = order_form(request.POST, request.FILES)
        if form_order.is_valid():
            the_order = form_order.save(commit=False)
            total = int(request.POST.get('category')) + int(request.POST.get('when'))
            the_order.order_total = total
            the_order.user_name = request.user.username
            the_order.user_email = request.user.email
            the_order.save()
            print(total)
            return redirect(reverse('payment'))

    else:
        form_order = order_form()

    return render(
        request, "../templates/order_work.html", {"form": form_order})
