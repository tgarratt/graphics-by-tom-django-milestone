from django.shortcuts import render, HttpResponse

# Create your views here.
def get_about_me(request):
    return render(request, "../templates/about_me.html")