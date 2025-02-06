from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'input'}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'textarea'}))
