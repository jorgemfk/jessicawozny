from django.db import migrations

def cargar_exposiciones_individuales(apps, schema_editor):
    Exposicion = apps.get_model('example', 'Exposicion')  # Reemplaza 'tu_app' con el nombre de tu app

    datos = [
        {"año": 2024, "nombre_exposicion": "Necesidades. Ejercicio en seco.",
         "lugar": "Rabia", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2023, "nombre_exposicion": "Paliativo. Ahora que estas en perfecto streamline.",
         "lugar": "Biblioteca Henestrosa/ Casa de la Ciudad", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2022, "nombre_exposicion": "Sanatorio Plateau. Teeth-as-tools. Dann bergabmi Affenzahn.",
         "lugar": "NONADA Gallery", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2020, "nombre_exposicion": "Ikat salvaje del telar domesticado.",
         "lugar": "Fly on the Wall project space, dentro del festival Oaxaca Múltiple", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2019, "nombre_exposicion": "Remedio casero. Ofrenda filigrana. Conjuro ahuehuete.",
         "lugar": "YOPEps, Yope Project Space", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2014, "nombre_exposicion": "Vista Panorámica de lo que solian llamar. Panoramic View of what they used to call.",
         "lugar": "Locker plant, Chinati Foundation", "estado": "Marfa, Texas", "pais": "USA", "tipo": "Individual"},

        {"año": 2009, "nombre_exposicion": "Last Drop First Flame",
         "lugar": "Deluge Contemporary Art", "estado": "Victoria, B.C.", "pais": "Canada", "tipo": "Individual"},

        {"año": 2007, "nombre_exposicion": "Vice & Virtue",
         "lugar": "Manuel García Contemporary Art", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2004, "nombre_exposicion": "Playground Heroes",
         "lugar": "Plan B Editions", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},

        {"año": 2004, "nombre_exposicion": "Hechizo Allianza B",
         "lugar": "Alianza Francesa", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},
        {"año": 2023, "nombre_exposicion": "FAMA Monterrey, Programa Carla",
         "lugar": "San Pedro Garza Garcia, Monterrey", "estado": "Nuevo León", "pais": "México", "tipo": "Colectiva"},

        {"año": 2023, "nombre_exposicion": "Globulo",
         "lugar": "Los Pinos Centro Cultural", "estado": "CDMX", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Guillermo Santamarina"},

        {"año": 2023, "nombre_exposicion": "Clavo Movimiento",
         "lugar": "Programa Carla / Espacio Lalitho", "estado": "CDMX", "pais": "México", "tipo": "Colectiva"},

        {"año": 2023, "nombre_exposicion": "Estación Material vol. 2",
         "lugar": "YOPE project space, Material Art Fair, Cerámica Suro", "estado": "Guadalajara", "pais": "México",
         "tipo": "Colectiva"},

        {"año": 2023, "nombre_exposicion": "Haiku Assembly No.1",
         "lugar": "Plan B", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva"},

        {"año": 2022, "nombre_exposicion": "Material Fair Vol.8",
         "lugar": "PEANA", "estado": "CDMX", "pais": "México", "tipo": "Colectiva"},

        {"año": 2021, "nombre_exposicion": "Cadena Infinita",
         "lugar": "Tubos y Conexiones", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva"},

        {"año": 2021, "nombre_exposicion": "OVNI: Observatorio de la voz de los niños y de la infancia",
         "lugar": "Diferentes espacios públicos en Oaxaca", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva"},

        {"año": 2021, "nombre_exposicion": "Units",
         "lugar": "Peana", "estado": "San Pedro Garza García", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Christian Camacho"},

        {"año": 2021, "nombre_exposicion": "Yo de ti / Tú de mí",
         "lugar": "Museo de Arte Contemporáneo (MACO)", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Blanca González"},

        {"año": 2021, "nombre_exposicion": "Don't get 2 close 2 my fantasy",
         "lugar": "Galería Karen Huber", "estado": "CDMX", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Endy Hupperich"},

        {"año": 2020, "nombre_exposicion": "Gran Sur, estados de ánimo fuera del centro",
         "lugar": "Museo Internacional del Barroco", "estado": "Puebla", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Gustavo Ramírez y Luis Hampshire"},

        {"año": 2019, "nombre_exposicion": "Dibujos de Sitio",
         "lugar": "Parallel///Oaxaca", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Oliver Martínez Kandt"},

        {"año": 2019, "nombre_exposicion": "Invisible Corpóreo",
         "lugar": "Casa Baltazar Centro Cultural", "estado": "Veracruz", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Luis Canseco"},

        {"año": 2018, "nombre_exposicion": "Escenarios Híbridos",
         "lugar": "MACO Museo de Arte Contemporáneo", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Itandéhui Méndez"},

        {"año": 2016, "nombre_exposicion": "Ediciones Eco 2",
         "lugar": "El ECO Museo Experimental", "estado": "CDMX", "pais": "México", "tipo": "Colectiva"},

        {"año": 2016, "nombre_exposicion": "Resonancias desde el jardín de las delicias",
         "lugar": "Museo de Arte Carrillo Gil", "estado": "CDMX", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Guillermo Santamarina"},

        {"año": 2014, "nombre_exposicion": "La voluntad de la piedra",
         "lugar": "Museo de Arte Carrillo Gil, Amparo Museum, MUSAS", "estado": "CDMX / Puebla / Hermosillo",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Catalina Lozano"},

        {"año": 2012, "nombre_exposicion": "10 Bienal FEMSA",
         "lugar": "MARCO", "estado": "Monterrey", "pais": "México", "tipo": "Colectiva"},

        {"año": 2009, "nombre_exposicion": "Incessant Flicker of Light",
         "lugar": "Punto Gallery, Sokei Academy of Arts", "estado": "Tokio", "pais": "Japón", "tipo": "Colectiva",
         "curaduria": "Himiko Takasawa"},

        {"año": 2008, "nombre_exposicion": "Estacionarte 08",
         "lugar": "Tlatelolco Cultural Center", "estado": "CDMX", "pais": "México", "tipo": "Colectiva"},

        {"año": 2006, "nombre_exposicion": "3a Bienal de Artes Visuales de Yucatán",
         "lugar": "Centro de las Artes", "estado": "Mérida, Yucatán", "pais": "México", "tipo": "Colectiva"},
    ]

    for dato in datos:
        Exposicion.objects.create(**dato)

    PremioDistincion = apps.get_model("example", "PremioDistincion")

    premios_iniciales = [
        {"año": "2021/2024", "distincion": "Miembro del SNCA, Artes Visuales/ Medios alternativos", "pais": "México"},
        {"año": "2014", "distincion": "Artist in Residence at the Chinati Foundation", "pais": "USA"},
        {"año": "2012-2014", "distincion": "Becaria del programa Bancomer M-ACG de Arte Actual", "pais": "México"},
        {"año": "2013",
         "distincion": "Artista en Residencia dentro del festival de artes Visuales Ciudad del Carmen (FAVCA)",
         "pais": "México"},
        {"año": "2007", "distincion": "Jóvenes Creadores, Arts (FOESCA)", "pais": "México"},
        {"año": "2006", "distincion": "Premio de Adquisición, 3a Bienal de Artes Visuales Yucatán", "pais": "México"},
        {"año": "2004", "distincion": "Mención Honorífica, 2a Bienal Nacional de Artes", "pais": "México"},
    ]

    for premio in premios_iniciales:
        PremioDistincion.objects.create(**premio)

class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_exposiciones_individuales),
    ]
