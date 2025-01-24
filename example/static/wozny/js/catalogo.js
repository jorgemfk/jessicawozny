const obras = [
    { nombre: "Herramienta madre", anio: 2020, imagen: "1.png", descripcion: "Pulpad epapelreciclado,alambre, piedraspómez,telamalla,tejidocrocheten hilometálico,tejidoscrochete nalgodón, poliéster, selladazo,rferdor esmalte de uñas, pintura vinilica, taponesde hule, globuli, pegamento,cantera", dimension: "90x75x95cm" },
    { nombre: "Ventana Oval", anio: 2024, imagen: "2.png", descripcion: "Estructuradeherrería,esmalte, allapnat denylon, fideosdenatación,placarecortadade espuma,alambrerecocidocubiertod epapel bubruaj y papel impreso en xeróx, engrudo , yeso piedra, arleamc obcreido ,cinta para enmascarillar,vendade o,yse o,sge tapa ed co,itáspl codo de plástico, muestra d e espuma con recubrimientode lentejauetlad, e sardinasalambrerecorceicduobierto dtee l aceong rudo , laminacorrugadadorada", dimension: "240x130x140com" },
    { nombre: "Steck portátil 2024(beige claro)", anio: 2024, imagen: "3.png", descripcion: "Escultura de viaje y escritorio(Diver) Jabonera de plastico, tejidos en algodón, poliester,alambrerecocido, arcillad epapel,esmalte de uñas", dimension: "8x11x4cm" },
    {
    nombre: "Retrato Madre e Hija de la serie Imitación",
    anio: 2024,
    descripcion: "Esmalte de uñas sobre papel.",
    dimension: "21×30 cm",
    imagen: "4.png"
  },
  {
    nombre: "Tremor patología",
    anio: 2023,
    descripcion: "Herrería forrada de volumen tejido crochet en algodón, plastificado y pintado con esmalte de uñas, poliéster, esferas de vidrio, lámina galvanizada en ángulo, impresiones xerox, engrudo, vibrador con control remoto, pulpa de papel, pegamento.",
    dimension: "100×80×50 cm",
    imagen: "5.png"
  },
  {
    nombre: "Sed interior insaciable y pequeña",
    anio: 2023,
    descripcion: "Tejido crochet plastificado, pintura, gesso, bolígrafo, tejido en gancho de lana, bordado sobre franela, pegamento, poliéster.",
    dimension: "23×15×10 cm",
    imagen: "6.png"
  },
  {
    nombre: "De la serie Sesiones/Sitzungen (temazcal cabeza perdida)",
    anio: 2022,
    descripcion: "Tejido de gancho en hilo de algodón desteñido, zacate, caucho negro, hilo encerado, alta temperatura, barro con reducción.",
    dimension: "32×30×8 m",
    imagen: "7.png"
  },
  {
    nombre: "Esquina L, corpúsculos y unsupported holding",
    anio: 2022,
    descripcion: "Pulpa de papel, encausto, tapones de hule, caucho, estopa, arcilla de papel, esmalte de uñas, fragmentos de vidrio, pegamento.",
    dimension: "80×80×40 cm",
    imagen: "8.png"
  },
  {
    nombre: "Ventanas deformes, cosas finitas y mundanas",
    anio: 2013,
    descripcion: "2 proyectores análogos hechizos, pantallas de poliestireno, empotradas en estructura de alambre recubierto, mesas hechas a la medida, plastilina, estopa, madera, alambre forrado y pintado, poliestireno expandido, estopa, dos cajas de madera con transparencias, impresión láser sobre acetato: Repertorio y Transcripción (el custodio elegirá las transparencias en su turno).",
    dimension: "400×400×170 cm",
    imagen: "9.png"
  },
  {
    nombre: "Partial reconstruction (Jumano)",
    anio: 2014,
    descripcion: "Plástico de pintor, tejidos de gancho plastificados, intervenidos, incrustaciones de piedras y residuos plásticos, pintados, de materiales encontrados, base giratoria, alambre, papel maché, pintura.",
    dimension: "200×200×350 cm",
    imagen: "10.png"
  },
  {
    nombre: "Culi intarsia",
    anio: 2013,
    descripcion: "Hecho de papel maché pintado, escritorio, foco, acrílico, borradores, metal, extensión.",
    dimension: "220×38×50 cm",
    imagen: "11.png"
  }
];

function cargarLista(orden) {
    document.getElementById("orden-alfabetico").classList.toggle("activo", orden === 'alfabetico');
    document.getElementById("orden-cronologico").classList.toggle("activo", orden === 'cronologico');

    const lista = document.getElementById("lista");
    lista.innerHTML = "";
    let obrasOrdenadas = [...obras];

    if (orden === "cronologico") {
        obrasOrdenadas.sort((a, b) => b.anio - a.anio);
    } else {
        obrasOrdenadas.sort((a, b) => a.nombre.localeCompare(b.nombre));
    }

    let indiceActual = null;
    obrasOrdenadas.forEach(obra => {
        let li = document.createElement("li");
        li.textContent = obra.nombre;

        if (orden === "cronologico") {
            if (indiceActual !== obra.anio) {
                let anioTitulo = document.createElement("li");
                anioTitulo.textContent = obra.anio;
                anioTitulo.style.fontSize = "1.5rem";
                anioTitulo.style.fontWeight = "bold";
                lista.appendChild(anioTitulo);
                indiceActual = obra.anio;
            }
        } else {
            let letra = obra.nombre[0].toUpperCase();
            if (indiceActual !== letra) {
                let letraTitulo = document.createElement("li");
                letraTitulo.textContent = letra;
                letraTitulo.style.fontSize = "1.5rem";
                letraTitulo.style.fontWeight = "bold";
                lista.appendChild(letraTitulo);
                indiceActual = letra;
            }
            li.textContent += ' ('+obra.anio+')';
        }

        li.addEventListener("mouseover", () => li.style.fontWeight = "bold");
        li.addEventListener("mouseout", () => li.style.fontWeight = "normal");
        li.addEventListener("click", () => mostrarObra(obra));
        lista.appendChild(li);
    });
}

function mostrarObra(obra) {
    document.getElementById("imagen").src = `/static/wozny/img/${obra.imagen}`;
    document.getElementById("titulo-obra").textContent = obra.nombre;
    document.getElementById("descripcion").textContent = obra.descripcion;
    document.getElementById("anio").textContent = obra.anio;
    document.getElementById("dimension").textContent = obra.dimension;
    document.querySelectorAll("lista-obras li").forEach(li => li.classList.remove("seleccionado"));
    event.target.classList.add("seleccionado");
}

function ordenar(criterio) {
    cargarLista(criterio);
}

document.addEventListener("DOMContentLoaded", () => {
    cargarLista("cronologico");
});
