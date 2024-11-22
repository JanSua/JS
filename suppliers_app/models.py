from django.db import models

# Create your models here.
class Supplier(models.Model):
    CompanyName = models.CharField(max_length=80)  # Campo obligatorio
    CompanyNIT = models.CharField(max_length=12)   # Campo obligatorio
    ContactPerson = models.CharField(max_length=80, blank=True)
    Tel1 = models.CharField(max_length=15, blank=True)
    Tel2 = models.CharField(max_length=15, blank=True)
    Email = models.CharField(max_length=80, blank=True)
    Ciudad = models.CharField(max_length=25, blank=True)
    Addrs = models.CharField(max_length=80, blank=True)
    Comment = models.TextField(blank=True)  # TextField para comentarios largos

    def __str__(self):
        return self.CompanyName
    
def upload_invoice(instance, filename):
    return f'invoices/{instance.supplier.CompanyName}/{filename}'


class Invoice(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='invoices')
    name = models.CharField(max_length=80, default="Factura", blank=True)  # Campo obligatorio
    date = models.DateField(blank=True)
    totalValue = models.IntegerField(default=0)
    paidValue = models.IntegerField(default=0)
    file = models.FileField(upload_to=upload_invoice, blank=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return f"Invoice {self.id} for {self.supplier.CompanyName}"
    
def upload_payment(instance, filename):
    return f'invoices/{instance.invoice.supplier.CompanyName}/{instance.invoice.date}/{filename}'

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField(blank=False, default='2024-01-01')
    paidValue = models.IntegerField(blank=False, default=0)
    file = models.FileField(upload_to=upload_payment, blank=True)
    