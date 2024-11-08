from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Supplier, Invoice
from .forms import CreateNewInvoice, CreateNewSupplier
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
    if request.method == 'POST':
        form = CreateNewInvoice(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Esto guarda la instancia de Invoice junto con el archivo y proveedor seleccionado
            return redirect('invoices')
    else:
        form = CreateNewInvoice()
    
    return render(request, "invoices/create_invoice.html", {
        'form': form
    })
    
def create_supplier(request):
    if request.method == 'GET':
        return render(request, "suppliers/create_supplier.html", {
            'form': CreateNewSupplier()
            })
    else:
        #print(request.POST)
        supplier = Supplier.objects.create(CompanyName=request.POST["companyName"], CompanyNIT=request.POST["companyNIT"], ContactPerson=request.POST["contactPerson"], Tel1=request.POST["tel1"], Tel2=request.POST["tel2"], Email=request.POST["email"], Ciudad=request.POST["ciudad"], Addrs=request.POST["addrs"], Comment=request.POST["comment"])
        return redirect('suppliers')
    
def supplier_detail(request, id):
    # supplier = Supplier.objects.get(id=id)
    supplier = get_object_or_404(Supplier, id=id)
    sup_invoices = Invoice.objects.filter(supplier_id=id)
    return render(request, "suppliers/detail.html", {
        'supplier' : supplier,
        'sup_invoices' : sup_invoices
    })