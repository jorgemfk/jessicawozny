const obras = [
    { nombre: "Obra A", anio: 1995, imagen: "obra1.jpg", descripcion: "Descripción de Obra A", tecnica: "Óleo sobre lienzo" },
    { nombre: "Obra B", anio: 2001, imagen: "1.png", descripcion: "Descripción de Obra B", tecnica: "Acrílico sobre madera" },
    { nombre: "Zbra C", anio: 1995, imagen: "obra2.jpg", descripcion: "Descripción de Obra C", tecnica: "Acrílico sobre madera" },
];

function cargarLista(orden) {
    document.getElementById("orden-alfabetico").classList.toggle("activo", orden === 'alfabetico');
    document.getElementById("orden-cronologico").classList.toggle("activo", orden === 'cronologico');

    const lista = document.getElementById("lista");
    lista.innerHTML = "";
    let obrasOrdenadas = [...obras];

    if (orden === "cronologico") {
        obrasOrdenadas.sort((a, b) => a.anio - b.anio);
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
    document.getElementById("tecnica").textContent = obra.tecnica;
}

function ordenar(criterio) {
    cargarLista(criterio);
}

document.addEventListener("DOMContentLoaded", () => {
    cargarLista("cronologico");
});
