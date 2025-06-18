from django.db import migrations

def cargar_exposiciones_individuales(apps, schema_editor):
    Exposicion = apps.get_model('example', 'Exposicion')  # Reemplaza 'tu_app' con el nombre de tu app

    datos = [
        {"año": 2024, "nombre_exposicion": "Necesidades. Ejercicio en seco", "lugar": "Rabia", "estado": "Oaxaca",
         "pais": "México", "tipo": "Individual"},
        {"año": 2023, "nombre_exposicion": "Paliativo. Ahora que estás en perfecto streamline",
         "lugar": "Biblioteca Henestrosa / Casa de la Ciudad", "estado": "Oaxaca", "pais": "México",
         "tipo": "Individual"},
        {"año": 2022, "nombre_exposicion": "Sanatorio Plateau. Teeth-as-tools. Dann bergab im Affenzahn",
         "lugar": "NONADA Gallery", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},
        {"año": 2020, "nombre_exposicion": "Ikat salvaje del telar domesticado",
         "lugar": "Fly on the Wall project space (Oaxaca Múltiple)", "estado": "Oaxaca", "pais": "México",
         "tipo": "Individual"},
        {"año": 2019, "nombre_exposicion": "Remedio casero. Ofrenda filigrana. Conjuro ahuehuete",
         "lugar": "YOPEps, Yope Project Space", "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},
        {"año": 2014, "nombre_exposicion": "Vista Panorámica de lo que solían llamar",
         "lugar": "Locker Plant, Chinati Foundation", "estado": "Texas", "pais": "USA", "tipo": "Individual"},
        {"año": 2009, "nombre_exposicion": "Last Drop First Flame", "lugar": "Deluge Contemporary Art",
         "estado": "British Columbia", "pais": "Canadá", "tipo": "Individual"},
        {"año": 2007, "nombre_exposicion": "Vice & Virtue", "lugar": "Manuel García Contemporary Art",
         "estado": "Oaxaca", "pais": "México", "tipo": "Individual"},
        {"año": 2004, "nombre_exposicion": "Playground Heroes", "lugar": "Plan B Editions", "estado": "Oaxaca",
         "pais": "México", "tipo": "Individual"},
        {"año": 2004, "nombre_exposicion": "Hechizo Allianza B", "lugar": "Alianza Francesa", "estado": "Oaxaca",
         "pais": "México", "tipo": "Individual"},

        {"año": 2025, "nombre_exposicion": "Jardín Vecino", "lugar": "Galería AP (UV)", "estado": "Veracruz",
             "pais": "México", "tipo": "Colectiva", "curaduria": "Andy Medina / Lisandro Santiago"},
        {"año": 2024, "nombre_exposicion": "Room Gymnastics. Gimnasia de salón", "lugar": "Casa Escuela",
             "estado": "Yucatán", "pais": "México", "tipo": "Colectiva",
             "curaduria": "Andrea Paasch y CO,MA Art Services"},
        {"año": 2024, "nombre_exposicion": "Todos somos de fuera", "lugar": "MACCO", "estado": "Oaxaca",
             "pais": "México", "tipo": "Colectiva"},
        {"año": 2023, "nombre_exposicion": "FAMA Monterrey, Programa Carla", "lugar": "San Pedro Garza García",
             "estado": "Nuevo León", "pais": "México", "tipo": "Colectiva"},
        {"año": 2023, "nombre_exposicion": "Globulo", "lugar": "Los Pinos Centro Cultural", "estado": "CDMX",
             "pais": "México", "tipo": "Colectiva", "curaduria": "Guillermo Santamarina"},
        {"año": 2023, "nombre_exposicion": "Clavo Movimiento", "lugar": "Programa Carla / Espacio Lalitho",
             "estado": "CDMX", "pais": "México", "tipo": "Colectiva"},
        {"año": 2023, "nombre_exposicion": "Estación Material vol. 2",
             "lugar": "YOPE project space, Material Art Fair, Cerámica Suro", "estado": "Guadalajara", "pais": "México",
             "tipo": "Colectiva"},
        {"año": 2023, "nombre_exposicion": "Haiku Assembly No.1", "lugar": "Plan B", "estado": "Oaxaca",
             "pais": "México", "tipo": "Colectiva"},
        {"año": 2022, "nombre_exposicion": "Material Fair Vol.8", "lugar": "PEANA", "estado": "CDMX",
             "pais": "México", "tipo": "Colectiva"},
        {"año": 2021, "nombre_exposicion": "Cadena Infinita", "lugar": "Tubos y Conexiones", "estado": "Oaxaca",
             "pais": "México", "tipo": "Colectiva", "curaduria": "Guadalajara 90210 / Andy Medina"},
        {"año": 2021, "nombre_exposicion": "OVNI: Observatorio de la voz de los niños y de la infancia",
             "lugar": "espacios públicos en Oaxaca (FILO 41)", "estado": "Oaxaca", "pais": "México",
             "tipo": "Colectiva", "curaduria": "Saúl Lopez Velarde"},
        {"año": 2021, "nombre_exposicion": "Units", "lugar": "Peana con Robert Janitz", "estado": "Nuevo León",
             "pais": "México", "tipo": "Colectiva", "curaduria": "Christian Camacho"},
        {"año": 2021, "nombre_exposicion": "Yo de ti / Tú de mí", "lugar": "Museo de Arte Contemporáneo MACO",
             "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva", "curaduria": "Blanca González"},
        {"año": 2021, "nombre_exposicion": "Don't get 2 close 2 my fantasy", "lugar": "Galería Karen Huber",
             "estado": "CDMX", "pais": "México", "tipo": "Colectiva", "curaduria": "Endy Hupperich"},
        {"año": 2020, "nombre_exposicion": "Gran Sur, estados de ánimo fuera del centro",
         "lugar": "Museo Internacional del Barroco", "estado": "Puebla", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Gustavo Ramírez y Luis Hampshire"},
        {"año": 2020, "nombre_exposicion": "Inverso Centro", "lugar": "NN Gallery", "estado": "Oaxaca",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Luis Hampshire"},
        {"año": 2019, "nombre_exposicion": "dibujos de Sitio", "lugar": "Parallel///Oaxaca", "estado": "Oaxaca",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Oliver Martinez Kandt"},
        {"año": 2019, "nombre_exposicion": "Invisible corpóreo", "lugar": "Casa Baltazar Centro Cultural",
         "estado": "Veracruz", "pais": "México", "tipo": "Colectiva", "curaduria": "Luis Canseco"},
        {"año": 2019, "nombre_exposicion": "Rudimentario", "lugar": "Rüido Projects", "estado": "Aguascalientes",
         "pais": "México", "tipo": "Colectiva"},
        {"año": 2018, "nombre_exposicion": "Escenarios Híbridos", "lugar": "Museo de Arte Contemporáneo MACO",
         "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva", "curaduria": "Itandéhui Méndez"},
        {"año": 2016, "nombre_exposicion": "Ediciones Eco 2", "lugar": "Museo Experimental El ECO", "estado": "CDMX",
         "pais": "México", "tipo": "Colectiva"},
        {"año": 2016, "nombre_exposicion": "Resonancias desde el jardín de las delicias",
         "lugar": "Museo de Arte Carrillo Gil", "estado": "CDMX", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Guillermo Santamarina Lagunes"},
        {"año": 2016, "nombre_exposicion": "La vieja revolución", "lugar": "Uno 61", "estado": "CDMX", "pais": "México",
         "tipo": "Colectiva", "curaduria": "Luis Hampshire"},
        {"año": 2015, "nombre_exposicion": "Reading Room A+WS", "lugar": "Aeromoto / Wendy's Subway during NADA",
         "estado": "New York", "pais": "USA", "tipo": "Colectiva"},
        {"año": 2014, "nombre_exposicion": "La voluntad de la piedra",
         "lugar": "Museo de Arte Carrillo Gil / Museo Amparo / MUSAS", "estado": "CDMX / Puebla / Hermosillo",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Catalina Lozano"},
        {"año": 2013, "nombre_exposicion": "Instantáneas de la diferencia: Un taller en el trópico",
         "lugar": "Taller Rufino Tamayo", "estado": "Oaxaca", "pais": "México", "tipo": "Colectiva"},
        {"año": 2012, "nombre_exposicion": "10 Bienal FEMSA", "lugar": "MARCO", "estado": "Monterrey", "pais": "México",
         "tipo": "Colectiva"},
        {"año": 2012, "nombre_exposicion": "Llaneza", "lugar": "Museo de Arte Contemporáneo MACO", "estado": "Oaxaca",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Carlos Ashida"},
        {"año": 2011, "nombre_exposicion": "Me gusta el plástico", "lugar": "MUPO", "estado": "Oaxaca",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Steffen Bödekker"},
        {"año": 2010, "nombre_exposicion": "Vice versa: nuevos estados de ánimo", "lugar": "MUPO", "estado": "Oaxaca",
         "pais": "México", "tipo": "Colectiva", "curaduria": "Luis Hampshire"},
        {"año": 2009, "nombre_exposicion": "Incesante parpadeo de Luz", "lugar": "Punto Gallery, Sokei Academy of Arts",
         "estado": "Tokyo", "pais": "Japón", "tipo": "Colectiva", "curaduria": "Himiko Takasawa"},
        {"año": 2009, "nombre_exposicion": "Second Meeting of Art and Contemporary Editions",
         "lugar": "NY Artbook Fair, P.S.1, MoMA", "estado": "New York", "pais": "USA", "tipo": "Colectiva"},
        {"año": 2009, "nombre_exposicion": "NOW. Transformation Spaces",
         "lugar": "UNAM, Casa del Lago Juan José Arreola", "estado": "CDMX", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Luisa Fuentes Guaza"},
        {"año": 2008, "nombre_exposicion": "Estacionarte 08", "lugar": "Centro Cultural Tlatelolco", "estado": "CDMX",
         "pais": "México", "tipo": "Colectiva"},
        {"año": 2008, "nombre_exposicion": "Ici et là-bas", "lugar": "Gallery de Villa de Guyancourt",
         "estado": "Guyancourt", "pais": "Francia", "tipo": "Colectiva", "curaduria": "Catalina Lozano"},
        {"año": 2006, "nombre_exposicion": "3a Bienal de Artes Visuales de Yucatán", "lugar": "Centro de las Artes",
         "estado": "Yucatán", "pais": "México", "tipo": "Colectiva"},
        {"año": 2006, "nombre_exposicion": "I love what you do", "lugar": "Drake A.I.R. Project, The Drake",
         "estado": "Toronto", "pais": "Canadá", "tipo": "Colectiva", "curaduria": "Nicole Rauffeisen y Ryan Witt"},
        {"año": 2006, "nombre_exposicion": "VII FEMSA Bienal Nacional", "lugar": "Centro de las Artes Monterrey",
         "estado": "Nuevo León", "pais": "México", "tipo": "Colectiva"},
        {"año": 2005, "nombre_exposicion": "Todo Terreno", "lugar": "MACO", "estado": "Oaxaca", "pais": "México",
         "tipo": "Colectiva"},
        {"año": 2004, "nombre_exposicion": "México 70: A decade within a generation",
         "lugar": "UNAM, Casa del Lago Juan José Arreola", "estado": "CDMX", "pais": "México", "tipo": "Colectiva",
         "curaduria": "Antonio Calera-Grobet y Eric Castillo Corona"},
        {"año": 2004, "nombre_exposicion": "2a Bienal Nacional de Yucatán", "lugar": "Instituto de Cultura de Yucatán",
         "estado": "Yucatán", "pais": "México", "tipo": "Colectiva"},
        {"año": 2003, "nombre_exposicion": "Superpop Ediciones", "lugar": "Plan B", "estado": "Oaxaca",
         "pais": "México", "tipo": "Colectiva"},
        {"año": 2002, "nombre_exposicion": "Sala de Recuperación", "lugar": "Museo de Arte Carrillo Gil",
         "estado": "CDMX", "pais": "México", "tipo": "Colectiva", "curaduria": "Paola Santoscoy y Gonzalo Ortega"},
        {"año": 2002, "nombre_exposicion": "Aktuelle Kunst aus Mexiko", "lugar": "Neue Galerie der HBK Braunschweig",
         "estado": "Braunschweig", "pais": "Alemania", "tipo": "Colectiva", "curaduria": "Abraham Cruzvillegas"},
        {"año": 2001, "nombre_exposicion": "Novísimos", "lugar": "MUCA", "estado": "CDMX", "pais": "México",
         "tipo": "Colectiva", "curaduria": "Abigail Maritxu Aranda Márquez"},
        {"año": 2000, "nombre_exposicion": "2nd Encuentro Transvolcánico", "lugar": "Universidad de las Américas",
         "estado": "Puebla", "pais": "México", "tipo": "Colectiva"}
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
def load_initial_acercade(apps, schema_editor):
    AcercaDe = apps.get_model('example', 'AcercaDe')
    AcercaDe.objects.create(
        acerca="Jessica Wozny nace en Langenfeld, Renania del Norte-Westfalia cerca de Colonia, Alemania,el día 28 de Febrero en  1978."
                +"Estudió la licenciatura de Lingüística, Romanística y Filosofía en Heinrich Heine Universität en Düsseldorf 1998/99."
                 ""
                +"Estudió la licenciatura en Artes Plásticas en la Escuela Nacional de Pintura, Escultura y Grabado ¨La Esmeralda¨ en la Ciudad de México (1999-2002)"
                +"Es co-fundadora junto con Luis Hampshire del proyecto curatorial Ediciones Plan B, 2004"
                +"Es fundadora de Nullnummern Press, editorial de publicaciones de artista, 2013. "
                +" Vive y trabaja desde 2003 en la Ciudad de Oaxaca""",
        otros_proyectos="""Wozny cuenta con diversas publicaciones y catálogos de su trabajo y es fundadora/editora de “Nullnummern Press“, proyecto de auto-publicación de artistaublicaciones de iniciado en el 2013
Participa en el proyecto La costumbre de los vientos dentro de la plataforma de investigación de pedagogía de arte: Organización auto-gestiva interdisciplinaria (OAI México), fundada y organizada por los artistas y docentes Liliana Ramales y Jorge Sosa.
( https://www.oaimexico.com/la-costumbre-de-los-vientos )
Wozny es creadora y hacedora de TULA, marca de muñecas-prototipo hechas de cerámica, trapo y up-cycling. ( https://instagram.com/tula_hechoamano )"""
)

def load_initial_statement(apps, schema_editor):
    Statement = apps.get_model('example', 'Statement')
    Statement.objects.create(
        texto="""Jessica Wozny (Langenfeld, Renania del Norte-Westfalia, Alemania, 1978) es artista visual y editora. Estudió Lingüística, Romanística y Filosofía en la Universidad Heinrich Heine de Düsseldorf, y la Licenciatura en Artes Plásticas en la ENPEG “La Esmeralda”, en la Ciudad de México. Desde 2003 vive y trabaja en Oaxaca, México.
        
Es cofundadora del proyecto curatorial Ediciones Plan B (2004) y fundadora de Nullnummern Press (2013), editorial dedicada a publicaciones de artista y procesos de autoedición. Su obra ha sido presentada en exposiciones individuales y colectivas en museos, ferias y espacios independientes en México, Estados Unidos, Alemania, Canadá, Francia y Japón.

Ha sido miembro del Sistema Nacional de Creadores de Arte (2021–2024) y becaria del programa Arte Actual Bancomer–MACG (2012–2014). En 2014 fue seleccionada como Artista en Residencia en la Chinati Foundation en Marfa, Texas, y en 2013 participó en una residencia de investigación artística en Ciudad del Carmen, 
Campeche, como parte del Festival de Artes Visuales de Campeche (FAVCA). En 2007 recibió la beca Jóvenes Creadores FOESCA en Oaxaca, y en 2006 obtuvo el premio de adquisición en la III Bienal Nacional de Artes Visuales de Yucatán."""

)



class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_exposiciones_individuales),
        migrations.RunPython(load_initial_acercade),
        migrations.RunPython(load_initial_statement)
    ]
