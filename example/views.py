from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import JsonResponse
import ssl
from django.views.decorators.csrf import csrf_exempt

from .models import Member

def index(request):
    #members = Member.objects.all()
    #member_list_html = [f"<li>{member.name}</li>" for member in members]
    #return HttpResponse(f"<ul>{''.join(member_list_html)}</ul>")
    return render(request, 'wozny/index.html')

def add_member(request, member_name):
    Member.objects.create(name=member_name)
    return redirect('index')


def catalogo(request):
    return render(request, 'wozny/catalogo.html')
def curriculum(request):
    return render(request, 'wozny/curriculum.html')

def contacto(request):
    if request.method == "POST":
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                message = form.cleaned_data["message"]

                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE  # Deshabilita verificación SSL

                send_mail(
                    subject="Nuevo mensaje de contacto",
                    message=f"Correo: {email}\n\nMensaje:\n{message}",
                    from_email=email,
                    recipient_list=["jorgemfk1@gmail.com"],  # Destinatario
                    fail_silently=False,
                )

                return JsonResponse({"success": True})
        except Exception as e:
            print(f"Error en la vista contacto: {e}")  # Ver error en la consola
            return JsonResponse({"error": "Error interno del servidor"}, status=500)
    return JsonResponse({"success": False, "error": "Error en el formulario."})