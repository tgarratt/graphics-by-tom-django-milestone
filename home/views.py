from django.shortcuts import render, HttpResponse

# Create your views here.
def get_home(request):
    return render(request, "../templates/home.html")