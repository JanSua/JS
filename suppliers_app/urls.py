from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('suppliers/<int:id>', views.supplier_detail, name="supplier_detail"),
    path('invoices/', views.invoices, name="invoices"),
    path('create_invoice/', views.create_invoice, name="create_invoice"),
    path('create_supplier/', views.create_supplier, name="create_supplier"),


]