from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Supplier, Invoice

def index(request):
    return render(request, "index.html")

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" %username)

def about(request):
    return render(request, "about.html")

def suppliers(request):
    suppliers = list(Supplier.objects.values())
    return render(request, "suppliers.html")

def invoices(request):
    # invoice = get_object_or_404(Invoice, id=id)
    return render(request, "invoices.html")