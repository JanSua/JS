from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Supplier, Invoice, Payment #Modelos
from .forms import CreateNewInvoice, CreateNewSupplier, CreateNewPayment
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
    # Capturar parámetros de ordenamiento
    sort_field = request.GET.get('sort', 'CompanyName')  # Campo por defecto
    order = request.GET.get('order', 'asc')  # Orden por defecto

    # Preparar el campo para orden ascendente o descendente
    if order == 'desc':
        sort_field = f"-{sort_field}"  # Prefijo "-" indica descendente

    # Obtener y ordenar los proveedores
    suppliers = Supplier.objects.all().order_by(sort_field)

    return render(request, "suppliers/suppliers.html", {
        'suppliers': suppliers,
        'current_sort': sort_field.lstrip('-'),
        'current_order': order
    })

def invoices(request):
    # invoice = get_object_or_404(Invoice, id=id)
    invoices = Invoice.objects.all()
    return render(request, "invoices/invoices.html", {
        'invoices': invoices
    })

def create_invoice(request, supplier_id, id=None):
    supplier = get_object_or_404(Supplier, id=supplier_id)  # Obtén el proveedor

    if id:
        # Si hay un ID, significa que estamos editando una factura existente
        invoice = get_object_or_404(Invoice, id=id, supplier=supplier)
    else:
        # Si no hay ID, estamos creando una nueva factura
        invoice = None

    if request.method == 'POST':
        form = CreateNewInvoice(request.POST, request.FILES, instance=invoice)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.supplier = supplier  # Asocia la factura al proveedor
            invoice.save()  # Guarda la factura
            return redirect('supplier_detail', id=supplier.id)  # Redirige al detalle del proveedor
        else:
            # Imprimir los errores del formulario para depuración
            print("Errores en el formulario:", form.errors)
    else:
        form = CreateNewInvoice(instance=invoice)

    return render(request, "invoices/create_invoice.html", {
        'form': form,
        'invoice': invoice,
        'supplier': supplier  # Pasamos el proveedor al contexto
    })





def delete_invoice(request, id):
    # Buscar la factura a eliminar
    invoice = get_object_or_404(Invoice, id=id)

    # Eliminar la factura
    invoice.delete()

    # Redirigir a la lista de facturas
    return redirect('supplier_detail', id=invoice.supplier_id)

def create_supplier(request, supplier_id=None):
    if supplier_id:  # Si se pasa un ID, buscamos el proveedor (modo edición)
        supplier = get_object_or_404(Supplier, id=supplier_id)
        form = CreateNewSupplier(initial={
            'companyName': supplier.CompanyName,
            'companyNIT': supplier.CompanyNIT,
            'contactPerson': supplier.ContactPerson,
            'tel1': supplier.Tel1,
            'tel2': supplier.Tel2,
            'email': supplier.Email,
            'ciudad': supplier.Ciudad,
            'addrs': supplier.Addrs,
            'comment': supplier.Comment,
        })
    else:  # Modo creación
        supplier = None
        form = CreateNewSupplier()

    if request.method == 'POST':
        form = CreateNewSupplier(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if supplier:  # Editando proveedor existente
                supplier.CompanyName = data['companyName']
                supplier.CompanyNIT = data['companyNIT']
                supplier.ContactPerson = data['contactPerson']
                supplier.Tel1 = data['tel1']
                supplier.Tel2 = data['tel2']
                supplier.Email = data['email']
                supplier.Ciudad = data['ciudad']
                supplier.Addrs = data['addrs']
                supplier.Comment = data['comment']
                supplier.save()
            else:  # Creando un nuevo proveedor
                Supplier.objects.create(
                    CompanyName=data['companyName'],
                    CompanyNIT=data['companyNIT'],
                    ContactPerson=data['contactPerson'],
                    Tel1=data['tel1'],
                    Tel2=data['tel2'],
                    Email=data['email'],
                    Ciudad=data['ciudad'],
                    Addrs=data['addrs'],
                    Comment=data['comment'],
                )
            return redirect('suppliers')  # Redirige a la lista de proveedores

    return render(request, 'suppliers/create_supplier.html', {'form': form, 'editing': bool(supplier)})



def supplier_detail(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    # Prefetch pagos relacionados con cada factura
    sup_invoices = Invoice.objects.filter(supplier_id=id).prefetch_related('payments')
    return render(request, "suppliers/detail.html", {
        'supplier': supplier,
        'sup_invoices': sup_invoices
    })
    
def delete_supplier(request, id):
    if request.method == "POST":
        supplier = get_object_or_404(Supplier, id=id)
        supplier.delete()
        return redirect('suppliers')
    return HttpResponse("Método no permitido", status=405)  

def create_payment(request, invoice_id):
    # Obtener la factura a partir de su ID
    invoice = get_object_or_404(Invoice, id=invoice_id)

    if request.method == 'POST':
        # Crear un formulario con los datos del POST
        form = CreateNewPayment(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guardamos el pago pero no lo commitimos inmediatamente
            payment = form.save(commit=False)
            # Relacionamos el pago con la factura
            payment.invoice = invoice
            payment.save()  # Guardamos el pago en la base de datos
            return redirect('supplier_detail', id=invoice.supplier.id)
    else:
        # Si el método es GET, simplemente mostramos el formulario vacío
        form = CreateNewPayment()

    return render(request, 'payments/create_payment.html', {
        'form': form,
        'invoice': invoice  # Pasamos la factura al contexto para usarla en el template
    })

#return redirect('supplier_detail', id=invoice.supplier.id)

def delete_payment(request, payment_id):
    if request.method == "POST":
        payment = get_object_or_404(Payment, id=payment_id)
        invoice = payment.invoice
        payment.delete()
        return redirect('supplier_detail', id=invoice.supplier_id)
    return HttpResponse("Método no permitido", status=405)  
 