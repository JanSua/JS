from django.contrib import admin
from .models import Payment, Supplier, Invoice
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Invoice)
admin.site.register(Payment)


