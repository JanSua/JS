from django import forms


class CreateNewInvoice(forms.Form):
    date = forms.DateField(label="Date of Invoice", widget = forms.DateInput(attrs={'class':'input'}))
    value = forms.IntegerField(label="Value of Invoice", widget = forms.NumberInput(attrs={'class':'input'}))
    file = forms.FileField(label="Upload File", widget = forms.FileInput(attrs={'class':'input'}))
    # TODO: Make the file save in the specified media folder.


class CreateNewSupplier(forms.Form):
    companyName = forms.CharField(label="Nombre compañía",max_length=80, widget = forms.TextInput(attrs={'class':'input'}))  # Campo obligatorio
    companyNIT = forms.CharField(label="NIT compañía",max_length=12, widget = forms.TextInput(attrs={'class':'input'}))   # Campo obligatorio
    contactPerson = forms.CharField(label="Nombre persona de contacto",max_length=80, required=False, widget = forms.TextInput(attrs={'class':'input'}))
    tel1 = forms.CharField(label="Teléfono de contacto 1",max_length=15, required=False, widget = forms.TextInput(attrs={'class':'input'}))
    tel2 = forms.CharField(label="Teléfono de contacto 2",max_length=15, required=False, widget = forms.TextInput(attrs={'class':'input'}))
    email = forms.CharField(label="Email",max_length=80, required=False, widget = forms.TextInput(attrs={'class':'input'}))
    ciudad = forms.CharField(label="Ciudad (principal) Compañía",max_length=25, required=False, widget = forms.TextInput(attrs={'class':'input'}))
    addrs = forms.CharField(label="Dirección Compañía",max_length=80, required=False, widget = forms.TextInput(attrs={'class':'input'}))
    comment = forms.CharField(label="Comentarios adicionales", required=False, widget = forms.Textarea(attrs={'class':'input'}))  # TextField para comentarios 

