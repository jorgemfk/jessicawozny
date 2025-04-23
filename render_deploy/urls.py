"""
URL configuration for render_deploy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example import views
from example.views import catalogo, curriculum
from example.views import contacto
from example.views import lista_premios, agregar_premio, editar_premio, eliminar_premio, admin_panel, subir_gif
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("add/<str:member_name>/", views.add_member, name="add_member"),
    path('catalogo/', catalogo, name='catalogo'),
    path('curriculum/', curriculum, name='curriculum'),
    path("contacto/", contacto, name="contacto"),
    path('exp/', views.lista_exposiciones, name='lista_exposiciones'),
    path('exp/agregar/', views.agregar_exposicion, name='agregar_exposicion'),
    path('exp/editar/<int:id>/', views.editar_exposicion, name='editar_exposicion'),
    path('exp/eliminar/<int:id>/', views.eliminar_exposicion, name='eliminar_exposicion'),
    path('exposiciones-individuales/', views.exposiciones_individuales, name='exposiciones_individuales'),
    path('exposiciones-json/', views.exposiciones_json, name='exposiciones_json'),
    path('dist/', lista_premios, name='lista_premios'),
    path('dist/nuevo/', agregar_premio, name='agregar_premio'),
    path('dist/editar/<int:premio_id>/', editar_premio, name='editar_premio'),
    path('dist/eliminar/<int:premio_id>/', eliminar_premio, name='eliminar_premio'),
    path('adm/', admin_panel, name='admin_panel'),
    path('subir/', views.subir_gif, name='subir_gif'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
