from django.shortcuts import render


def get_about_me(request):
    # returns the about Tom page
    return render(request, "../templates/about_me.html")
