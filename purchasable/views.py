from django.shortcuts import render, HttpResponse

# Create your views here.
def get_purchasable(request):
    return render(request, "../templates/purchasable.html")