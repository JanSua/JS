from django import forms
from .models import Invoice, Supplier
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CreateNewInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['supplier', 'date', 'totalValue', 'paidValue', 'file', 'paid']
        labels = {
            'supplier': 'Select Supplier',
            'date': 'Date of Invoice',
            'totalValue': 'Value of Invoice',
            'paidValue' : 'Paid value' , 
            'file': 'Upload File',
            'paid': 'Status of Invoice',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'totalvalue': forms.NumberInput(attrs={'class': 'input'}),
            'paidvalue': forms.NumberInput(attrs={'class': 'input'}),
            'file': forms.FileInput(attrs={'class': 'input'}),
            'paid': forms.CheckboxInput(attrs={'class': 'input'}),
        }
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), label="Supplier", widget=forms.Select(attrs={'class': 'input'}))



class CreateNewSupplier(forms.Form):
    companyName = forms.CharField(label="Nombre compañía",max_length=80, widget = forms.TextInput(attrs={'class':'form-control'}))  # Campo obligatorio
    companyNIT = forms.CharField(label="NIT compañía",max_length=12, widget = forms.TextInput(attrs={'class':'form-control'}))   # Campo obligatorio
    contactPerson = forms.CharField(label="Nombre persona de contacto",max_length=80, required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    tel1 = forms.CharField(label="Teléfono de contacto 1",max_length=15, required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    tel2 = forms.CharField(label="Teléfono de contacto 2",max_length=15, required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email",max_length=80, required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    ciudad = forms.CharField(label="Ciudad (principal) Compañía",max_length=25, required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    addrs = forms.CharField(label="Dirección Compañía",max_length=80, required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    comment = forms.CharField(label="Comentarios adicionales", required=False, widget = forms.Textarea(attrs={'class':'form-control'}))  # TextField para comentarios 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'Guardar'))

