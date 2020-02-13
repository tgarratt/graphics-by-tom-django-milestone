from django.shortcuts import render, HttpResponse
from unpurchasable_form.models import add_piece


def get_unpurchasable(request):
    add_pieces = add_piece.objects.all()
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})

    