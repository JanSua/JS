from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Supplier, Invoice
from .forms import CreateNewInvoice
def index(request):
    title = "Welcome Django!!¡¡"
    return render(request, "index.html", {
        'titulo': title,
    })

def about(request):
    username = "JanSua"
    return render(request, "about.html", {
        'username': username,
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" %username)


def suppliers(request):
    # suppliers = list(Supplier.objects.values())
    suppliers = Supplier.objects.all()
    return render(request, "suppliers/suppliers.html", {
        'suppliers' : suppliers
    })

def invoices(request):
    # invoice = get_object_or_404(Invoice, id=id)
    invoices = Invoice.objects.all()
    return render(request, "invoices/invoices.html", {
        'invoices': invoices
    })

def create_invoice(request):
    if request.method == 'GET':
        return render(request, "invoices/create_invoice.html", {
        'form': CreateNewInvoice()
    })
    else:
        Invoice.objects.create(date=request.POST['date'], value=request.POST['value'], file=request.POST['file'], supplier_id = 3)
        return redirect('/invoices')
    
