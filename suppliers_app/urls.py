from django.urls import path
from . import views

urlpatterns = [
    # Genéricos
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    #Suppliers
    #path('create_supplier/', views.create_supplier, name="create_supplier"),
    path('delete_supplier/<int:id>', views.delete_supplier, name="supplier_delete"),
    path('supplier/new/', views.create_supplier, name='create_supplier'),
    path('supplier/edit/<int:supplier_id>/', views.create_supplier, name='edit_supplier'),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('suppliers/<int:id>', views.supplier_detail, name="supplier_detail"),
    #Invoices
    path('invoices/', views.invoices, name="invoices"),
    path('create_invoice/<int:supplier_id>/', views.create_invoice, name="create_invoice"),
    path('edit_invoice/<int:supplier_id>/<int:id>/', views.create_invoice, name='edit_invoice'),
    path('delete_invoice/<int:id>/', views.delete_invoice, name='delete_invoice'),
    #Payments
    path('create_payment/<int:invoice_id>/', views.create_payment, name='create_payment'),
    path('delete_payment/<int:id>', views.delete_payment, name="delete_payment"),
    
    
    


]