from django.shortcuts import render, redirect, reverse, get_object_or_404
from unpurchasable_form.models import add_piece


def get_unpurchasable(request):
    add_pieces = add_piece.objects.all()
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_piece(request, pk):
    piece = get_object_or_404(add_piece, pk=pk)
    context = {
        "piece": piece
    }

    return render(request, "../templates/unpurchasable_piece.html", context)


def get_unpurchasable_piece_delete(request, pk=None):
    delete_piece = get_object_or_404(add_piece, pk=pk)
    delete_piece.delete()

    return redirect(reverse('unpurchasable'))
