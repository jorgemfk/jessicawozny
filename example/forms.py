from django import forms
from .models import Exposicion
from .models import PremioDistincion

class ContactForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'input'}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'textarea'}))

class ExposicionForm(forms.ModelForm):
    class Meta:
        model = Exposicion
        fields = ['año', 'nombre_exposicion', 'lugar', 'estado', 'pais', 'curaduria', 'tipo']
        widgets = {
            'tipo': forms.Select(choices=Exposicion.TIPO_CHOICES, attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_exposicion': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'curaduria': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PremioDistincionForm(forms.ModelForm):
    class Meta:
        model = PremioDistincion
        fields = ['año', 'distincion', 'pais']