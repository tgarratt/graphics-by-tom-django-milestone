from django.shortcuts import render, redirect, reverse
from .forms import add_piece_form


def get_unpurchasable_form(request):
    # display form allowing admin to add items to the previous work page
    if request.method == "POST":
        form_add = add_piece_form(request.POST, request.FILES)
        if form_add.is_valid():
            form_add.save()
            return redirect(reverse('unpurchasable'))

    else:
        form_add = add_piece_form()

    return render(
        request, "../templates/unpurchasable_form.html", {"form": form_add})
