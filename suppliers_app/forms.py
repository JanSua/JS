from django import forms


class CreateNewInvoice(forms.Form):
    date = forms.DateField(label="Date of Invoice")
    value = forms.IntegerField(label="Value of Invoice")
    file = forms.FileField(label="Upload File")

'''
class CreateNewSupplier(forms.Form):
    CompanyName = forms.CharField(max_length=80)  # Campo obligatorio
    CompanyNIT = forms.CharField(max_length=12)   # Campo obligatorio
    ContactPerson = forms.CharField(max_length=80, blank=True)
    Tel1 = forms.CharField(max_length=15, blank=True)
    Tel2 = forms.CharField(max_length=15, blank=True)
    Email = forms.CharField(max_length=80, blank=True)
    Ciudad = forms.CharField(max_length=25, blank=True)
    Addrs = forms.CharField(max_length=80, blank=True)
    Comment = forms.TextField(blank=True)  # TextField para comentarios 
'''
