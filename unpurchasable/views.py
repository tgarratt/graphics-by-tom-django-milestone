from django.shortcuts import render, HttpResponse

# Create your views here.
def get_unpurchasable(request):
    return render(request, "../templates/unpurchasable.html")