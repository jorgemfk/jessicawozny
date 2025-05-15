const obras = [];

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
        li.textContent = obra.nombre +' ('+obra.anio+')';
        /*
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
        }*/

        li.addEventListener("mouseover", () => li.style.fontWeight = "bold");
        li.addEventListener("mouseout", () => li.style.fontWeight = "normal");
        li.addEventListener("click", () => mostrarObra(obra));
        lista.appendChild(li);

    });
    mostrarObra(obrasOrdenadas[0]);
}

function mostrarObra(obra) {
    document.getElementById("imagen").src = `/media/${obra.id}/${obra.id}_1_1.png`;
    document.getElementById("titulo-obra").textContent = obra.nombre;
    document.getElementById("descripcion").textContent = obra.descripcion;
    document.getElementById("coleccion").textContent = obra.coleccion;
    document.getElementById("anio").textContent = obra.anio;
    document.getElementById("dimension").textContent = obra.dimension;
    const trabajoId = obra.id;
    const thumbnailsContainer = document.querySelector('.thumbnails');
    const imagenPrincipal = document.getElementById('imagen');
    thumbnailsContainer.innerHTML = '';
    // Cargar thumbnails desde el endpoint JSON
    fetch(`/cata/${trabajoId}/imagenes-tumb-json/`)
        .then(response => response.json())
        .then(data => {
            data.imagenes.forEach(url => {
                const img = document.createElement('img');
                img.src = url;
                img.className = 'thumb';
                img.style.width = '40px';
                img.style.cursor = 'pointer';
                img.onclick = () => {
                    // Cambia _2.png por _1.png para cargar la imagen ampliada
                    const ampliada = url.replace('_2.png', '_1.png');
                    imagenPrincipal.src = ampliada;
                };
                thumbnailsContainer.appendChild(img);
            });

            // Opcional: mostrar la primera imagen como ampliada por defecto
            if (data.imagenes.length > 0) {
                imagenPrincipal.src = data.imagenes[0].replace('_2.png', '_1.png');
            }
        })
        .catch(error => console.error('Error cargando imágenes:', error));
    //document.querySelectorAll("lista-obras li").forEach(li => li.classList.remove("seleccionado"));
    event.target.classList.add("seleccionado");
}

function ordenar(criterio) {
    cargarLista(criterio);
}

document.addEventListener("DOMContentLoaded", function () {
        fetch("/trabajos-json/")
            .then(response => response.json())
            .then(data => {
                // Llenar las listas con los datos obtenidos
                obras.push(...data.trabajos);

                console.log("trabajos:", obras);
                cargarLista("cronologico");
            })
            .catch(error => console.error("Error al cargar trabajos:", error));
        });
