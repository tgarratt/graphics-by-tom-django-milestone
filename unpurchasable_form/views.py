from django.shortcuts import render, HttpResponse
from .forms import add_piece_form


def get_unpurchasable_form(request):
    if request.method == "POST":
        form_add = add_piece_form(request.POST, request.FILES)
        if form_add.is_valid():
            form_add.save()
            print("Success")

    else:
        form_add = add_piece_form()

    return render(
        request, "../templates/unpurchasable_form.html", {"form": form_add})
