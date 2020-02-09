from django.shortcuts import render, HttpResponse
from .forms import order_form

# Create your views here.
def get_order_work(request):
    if request.method == "POST":
        form = order_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Success")

    else:
        form = order_form()


    return render(request, "../templates/order_work.html", {"form": form})