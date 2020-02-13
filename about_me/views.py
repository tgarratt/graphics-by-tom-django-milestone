from django.shortcuts import render, HttpResponse


def get_about_me(request):
    return render(request, "../templates/about_me.html")