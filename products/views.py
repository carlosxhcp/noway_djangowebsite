from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_product(request):
    return render (request, 'add_product.html')