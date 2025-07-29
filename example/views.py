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
from .models import Member
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajo
from .forms import TrabajoForm
from PIL import Image
import os
from django.conf import settings
from .forms import GifForm
from .models import AcercaDe, Statement, Serie
from .forms import AcercaDeForm, StatementForm, SerieForm

def editar_statement(request):
    statement = Statement.objects.last()
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES, instance=statement)
        if form.is_valid():
            form.save()
            return redirect('ver_statement')
    else:
        form = StatementForm(instance=statement)
    return render(request, 'admin/edit_statement.html', {'form': form})

# Vista para mostrar el Statement

def ver_statement(request):
    statement = Statement.objects.last()
    return render(request, 'wozny/statement.html', {'statement': statement})

def obtener_acercade_json(request):
    try:
        ultimo = AcercaDe.objects.latest('actualizado')
        data = {
            'acerca': ultimo.acerca,
            'otros_proyectos': ultimo.otros_proyectos,
        }
    except AcercaDe.DoesNotExist:
        data = {
            'acerca': '',
            'otros_proyectos': '',
        }
    return JsonResponse(data)

def editar_acerca_de(request):
    instancia, creado = AcercaDe.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = AcercaDeForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('editar_acerca_de')
    else:
        form = AcercaDeForm(instance=instancia)

    return render(request, 'exposiciones/acercade.html', {'form': form})

# Vista para listar todos los trabajos
def lista_trabajos(request):
    trabajos = Trabajo.objects.all()
    return render(request, 'trabajos/lista.html', {'trabajos': trabajos})

# Vista para crear un nuevo trabajo
def crear_trabajo(request):
    if request.method == 'POST':
        form = TrabajoForm(request.POST, request.FILES)
        if form.is_valid():
            trabajo = form.save()

            files = request.FILES.getlist('imagenes')
            for i, file in enumerate(files):
                numero = i + 1
                base_path = f"{trabajo.id}/{trabajo.id}_{numero}_"

                # Crear carpeta si no existe
                output_dir = os.path.join(settings.MEDIA_ROOT, str(trabajo.id))
                os.makedirs(output_dir, exist_ok=True)

                # Imagen principal (1600px)
                img = Image.open(file)
                img = img.convert('RGBA') if file.name.endswith('.png') else img.convert('RGB')
                img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                main_filename = f"{base_path}1.png"
                main_path = os.path.join(settings.MEDIA_ROOT, main_filename)
                img.save(main_path, 'PNG')

                # Imagen reducida (40px)
                img.thumbnail((40, 40), Image.Resampling.LANCZOS)
                thumb_filename = f"{base_path}2.png"
                thumb_path = os.path.join(settings.MEDIA_ROOT, thumb_filename)
                img.save(thumb_path, 'PNG')

            return redirect('lista_trabajos')
    else:
        form = TrabajoForm()
    return render(request, 'trabajos/crear.html', {'form': form})

# Vista para editar un trabajo existente
def editar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    if request.method == 'POST':
        form = TrabajoForm(request.POST, request.FILES, instance=trabajo)
        if form.is_valid():
            form.save()
            files = request.FILES.getlist('imagenes')
            existing_count = len([f for f in os.listdir(os.path.join(settings.MEDIA_ROOT, str(trabajo.id))) if f.endswith('_1.png')])
            for i, file in enumerate(files):
                numero = existing_count + i + 1
                base_path = f"{trabajo.id}/{trabajo.id}_{numero}_"
                output_dir = os.path.join(settings.MEDIA_ROOT, str(trabajo.id))
                os.makedirs(output_dir, exist_ok=True)
                img = Image.open(file)
                img = img.convert('RGBA') if file.name.endswith('.png') else img.convert('RGB')
                img.thumbnail((1600, 1600), Image.LANCZOS)
                main_filename = f"{base_path}1.png"
                main_path = os.path.join(settings.MEDIA_ROOT, main_filename)
                img.save(main_path, 'PNG')
                img.thumbnail((40, 40), Image.LANCZOS)
                thumb_filename = f"{base_path}2.png"
                thumb_path = os.path.join(settings.MEDIA_ROOT, thumb_filename)
                img.save(thumb_path, 'PNG')
            return redirect('lista_trabajos')
    else:
        form = TrabajoForm(instance=trabajo)

    imagenes_dir = os.path.join(settings.MEDIA_ROOT, str(trabajo.id))
    imagenes = []
    if os.path.exists(imagenes_dir):
        imagenes = [f"/media/{trabajo.id}/{f}" for f in os.listdir(imagenes_dir) if f.endswith('_2.png')]

    return render(request, 'trabajos/editar.html', {'form': form, 'trabajo': trabajo, 'imagenes': imagenes})
# API para eliminar imagen individual
def eliminar_imagen(request):
    if request.method == 'POST':
        image_path = request.POST.get('path')
        if image_path:
            main_path = image_path.replace('_2.png', '_1.png').replace('/media/', settings.MEDIA_ROOT + '/')
            thumb_path = image_path.replace('/media/', settings.MEDIA_ROOT + '/')
            if os.path.exists(main_path):
                os.remove(main_path)
            if os.path.exists(thumb_path):
                os.remove(thumb_path)
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

# Vista para eliminar un trabajo
def eliminar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    if request.method == 'POST':
        trabajo.delete()
        return redirect('lista_trabajos')
    return render(request, 'trabajos/eliminar.html', {'trabajo': trabajo})

def index(request):
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

def trabajos_json(request):
    # Trabajos sin serie
    trabajos = list(
        Trabajo.objects.filter(serie__isnull=True)
        .order_by('-anio')
        .values('id', 'nombre', 'anio', 'descripcion', 'dimension')
    )
    for t in trabajos:
        t['tipo'] = 0  # indicador de trabajo

    # Series con sus trabajos
    series = []
    for serie in Serie.objects.all().order_by('-anio'):
        trabajos_serie = list(
            serie.trabajos.all()
            .order_by('-nombre')
            .values('id', 'nombre', 'anio', 'descripcion', 'dimension')
        )
        for t in trabajos_serie:
            t['tipo'] = 0  # mantener consistencia si los recorres después

        series.append({
            'id': serie.id,
            'nombre': serie.nombre,
            'anio': serie.anio,
            'descripcion': serie.descripcion,
            'dimension': serie.dimension,
            'tipo': 1,  # indicador de serie
            'trabajos': trabajos_serie
        })

    # Combinamos ambos
    data = trabajos + series
    return JsonResponse({'items': data})

def imagenes_tumb_json(request, trabajo_id):
    carpeta = os.path.join(settings.MEDIA_ROOT, str(trabajo_id))
    if not os.path.exists(carpeta):
        return JsonResponse({'imagenes': []})

    archivos = os.listdir(carpeta)
    imagenes = []
    for archivo in archivos:
        if archivo.endswith('_2.png'):
            url = f"{settings.MEDIA_URL}{trabajo_id}/{archivo}"
            imagenes.append(url)

    return JsonResponse({'imagenes': imagenes})

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


def lista_series(request):
    series = Serie.objects.all()
    return render(request, 'series/lista_series.html', {'series': series})

def crear_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            serie = form.save(commit=False)
            serie.save()
            serie.trabajos.set(form.cleaned_data['trabajos'])
            return redirect('lista_series')
    else:
        form = SerieForm()
    return render(request, 'series/crear_serie.html', {'form': form})

def editar_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    if request.method == 'POST':
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            serie = form.save(commit=False)
            serie.save()
            serie.trabajos.set(form.cleaned_data['trabajos'])
            return redirect('lista_series')
    else:
        form = SerieForm(instance=serie)
    return render(request, 'series/editar_serie.html', {'form': form, 'serie': serie})

def eliminar_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    if request.method == 'POST':
        serie.delete()
        return redirect('lista_series')
    return render(request, 'series/eliminar_serie.html', {'serie': serie})
