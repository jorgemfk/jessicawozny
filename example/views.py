from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import JsonResponse
import ssl
from django.views.decorators.csrf import csrf_exempt
from .models import Exposicion
from .forms import ExposicionForm
from .models import PremioDistincion
from .forms import PremioDistincionForm
from .models import Gif
from .forms import GifForm

from .models import Member

def index(request):
    #members = Member.objects.all()
    #member_list_html = [f"<li>{member.name}</li>" for member in members]
    #return HttpResponse(f"<ul>{''.join(member_list_html)}</ul>")
    print("ates")
    gif = Gif.objects.last()  # Asume que solo hay uno o quieres mostrar el más reciente
    print(gif)
    return render(request, 'wozny/index.html', {'gif': gif})

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



def lista_exposiciones(request):
    exposiciones = Exposicion.objects.all().order_by('tipo', '-año')
    return render(request, 'exposiciones/lista.html', {'exposiciones': exposiciones})

def agregar_exposicion(request):
    if request.method == 'POST':
        form = ExposicionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_exposiciones')
    else:
        form = ExposicionForm()
    return render(request, 'exposiciones/form.html', {'form': form, 'titulo': 'Agregar Exposición'})

def editar_exposicion(request, id):
    exposicion = get_object_or_404(Exposicion, id=id)
    if request.method == 'POST':
        form = ExposicionForm(request.POST, instance=exposicion)
        if form.is_valid():
            form.save()
            return redirect('lista_exposiciones')
    else:
        form = ExposicionForm(instance=exposicion)
    return render(request, 'exposiciones/form.html', {'form': form, 'titulo': 'Editar Exposición'})

def eliminar_exposicion(request, id):
    exposicion = get_object_or_404(Exposicion, id=id)
    if request.method == 'POST':
        exposicion.delete()
        return redirect('lista_exposiciones')
    return render(request, 'exposiciones/eliminar.html', {'exposicion': exposicion})

def exposiciones_individuales(request):
    exposiciones = Exposicion.objects.filter(tipo="Individual").values(
        "año", "nombre_exposicion", "lugar", "estado", "pais"
    )
    return JsonResponse(list(exposiciones), safe=False)


def exposiciones_json(request):
    exposiciones_individuales = list(Exposicion.objects.filter(tipo="Individual").values(
        "año", "nombre_exposicion", "lugar", "estado", "pais", "curaduria"
    ))

    exposiciones_colectivas = list(Exposicion.objects.filter(tipo="Colectiva").values(
        "año", "nombre_exposicion", "lugar", "estado", "pais", "curaduria"
    ))

    premios = list(PremioDistincion.objects.all().order_by('-año').values(
        'año', 'distincion', 'pais'
    ))
    return JsonResponse({
        "individuales": exposiciones_individuales,
        "colectivas": exposiciones_colectivas,
        "premios": premios
    })

def lista_premios(request):
    premios = PremioDistincion.objects.all().order_by('-año')
    return render(request, 'premios/lista.html', {'premios': premios})

def agregar_premio(request):
    if request.method == 'POST':
        form = PremioDistincionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_premios')
    else:
        form = PremioDistincionForm()
    return render(request, 'premios/formulario.html', {'form': form})

def editar_premio(request, premio_id):
    premio = get_object_or_404(PremioDistincion, id=premio_id)
    if request.method == 'POST':
        form = PremioDistincionForm(request.POST, instance=premio)
        if form.is_valid():
            form.save()
            return redirect('lista_premios')
    else:
        form = PremioDistincionForm(instance=premio)
    return render(request, 'premios/formulario.html', {'form': form})

def eliminar_premio(request, premio_id):
    premio = get_object_or_404(PremioDistincion, id=premio_id)
    if request.method == 'POST':
        premio.delete()
        return redirect('lista_premios')
    return render(request, 'premios/confirmar_eliminar.html', {'premio': premio})

def admin_panel(request):
    return render(request, 'admin/admin_panel.html')

from .forms import GifForm
from .models import GifAnimacion

def subir_gif(request):
    if request.method == 'POST':
        Gif.objects.all().delete()  # Elimina todos los anteriores si solo debe haber uno
        form = GifForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Regresa a mostrar_gif.html
    else:
        form = GifForm()
    return render(request, 'admin/subir_portada.html', {'form': form})