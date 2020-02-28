from django.shortcuts import render


def get_home(request):
    # returns homepage
    return render(request, "../templates/home.html")
