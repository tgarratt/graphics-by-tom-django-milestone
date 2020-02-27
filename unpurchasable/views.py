from django.shortcuts import render, redirect, reverse, get_object_or_404
from unpurchasable_form.models import add_piece
from unpurchasable_form.forms import add_piece_form


def get_unpurchasable(request):
    # all
    add_pieces = add_piece.objects.all()
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_logo(request):
    # logo
    add_pieces = add_piece.objects.filter(piece_category="25")
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_clothing(request):
    # clothing
    add_pieces = add_piece.objects.filter(piece_category="20")
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_web_app(request):
    # web app
    add_pieces = add_piece.objects.filter(piece_category="30")
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_advertising(request):
    # advertising
    add_pieces = add_piece.objects.filter(piece_category="35")
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_illustration(request):
    # illustration
    add_pieces = add_piece.objects.filter(piece_category="40")
    return render(
        request, "../templates/unpurchasable.html", {"add_pieces": add_pieces})


def get_unpurchasable_packaging(request):
    # packaging
    add_pieces = add_piece.objects.filter(piece_category="15")
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


def get_unpurchasable_piece_edit(request, pk):
    edit_info = get_object_or_404(add_piece, pk=pk)
    print(edit_info)

    if request.method == "POST":

        form_edit = add_piece_form(request.POST, request.FILES, instance=edit_info)
        if form_edit.is_valid():
            edit_info = form_edit.save(commit=False)
            form_edit.save()
            return redirect(reverse('unpurchasable'))

    else:
        form_edit = add_piece_form(instance=edit_info)

    return render(request, "../templates/unpurchasable_edit.html", {"form_edit": form_edit})