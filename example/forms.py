from django import forms
from .models import Exposicion
from .models import PremioDistincion
from .models import Gif
from .models import Trabajo

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
        widgets = {
            'año': forms.TextInput(attrs={'class': 'form-control'}),
            'distincion': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ['archivo']

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class TrabajoForm(forms.ModelForm):
    imagenes = MultipleFileField(label='Select files', required=False)

    class Meta:
        model = Trabajo
        fields = ['nombre', 'anio', 'descripcion', 'dimension','coleccion']
        widgets = {
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dimension': forms.TextInput(attrs={'class': 'form-control'}),
            'coleccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
