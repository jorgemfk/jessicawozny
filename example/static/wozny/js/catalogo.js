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

function cargarFicha(obra) {
    // Actualizar ficha técnica
   const ficha = document.getElementById("ficha-tecnica");
   ficha.textContent = `${obra.nombre || ''}, ${obra.anio || ''}, ${obra.descripcion || ''}, ${obra.dimension || ''}`;

}
function mostrarObra(obra) {
    const imagenPrincipal = document.getElementById("imagen");
    const thumbnailsContainer = document.querySelector('.thumbnails');

    document.getElementById("titulo-obra").textContent = obra.nombre;
    document.getElementById("descripcion").textContent = obra.descripcion;
    document.getElementById("anio").textContent = obra.anio;
    document.getElementById("dimension").textContent = obra.dimension;
    document.getElementById("coleccion").textContent = obra.coleccion || '';

    thumbnailsContainer.innerHTML = '';

    if (obra.tipo === 0) {
        // Es un trabajo individual
        imagenPrincipal.src = `/media/${obra.id}/${obra.id}_1_1.png`;
        fetch(`/cata/${obra.id}/imagenes-tumb-json/`)
            .then(response => response.json())
            .then(data => {
                data.imagenes.forEach(url => {
                    const img = document.createElement('img');
                    img.src = url;
                    img.className = 'thumb';
                    img.style.width = '40px';
                    img.style.cursor = 'pointer';
                    img.onclick = () => {
                        imagenPrincipal.src = url.replace('_2.png', '_1.png');

                    };
                    thumbnailsContainer.appendChild(img);
                });
                if (data.imagenes.length > 0) {
                    imagenPrincipal.src = data.imagenes[0].replace('_2.png', '_1.png');
                }
            })
            .catch(error => console.error('Error cargando imágenes:', error));

    } else if (obra.tipo === 1 && obra.trabajos.length > 0) {
        // Es una serie, usamos el primer trabajo
        const primerTrabajo = obra.trabajos[0];
        imagenPrincipal.src = `/media/${primerTrabajo.id}/${primerTrabajo.id}_1_1.png`;

        // Cargar thumbnails de todos los trabajos de la serie
        obra.trabajos.forEach(trabajo => {
            fetch(`/cata/${trabajo.id}/imagenes-tumb-json/`)
                .then(response => response.json())
                .then(data => {
                    data.imagenes.forEach(url => {
                        const img = document.createElement('img');
                        img.src = url;
                        img.className = 'thumb';
                        img.style.width = '40px';
                        img.style.cursor = 'pointer';
                        img.onclick = () => {
                            imagenPrincipal.src = url.replace('_2.png', '_1.png');
                            cargarFicha(trabajo);
                        };
                        thumbnailsContainer.appendChild(img);
                    });
                })
                .catch(error => console.error('Error cargando imágenes de trabajo en serie:', error));
        });
    }

    // Marcar seleccionado
    //document.querySelectorAll(".lista-obras li").forEach(li => li.classList.remove("seleccionado"));
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
                obras.push(...data.items);

                console.log("trabajos:", obras);
                const spinner = document.getElementById("spinner");
                spinner.style.display = "none";
                cargarLista("cronologico");

            })
            .catch(error => console.error("Error al cargar trabajos:", error));
        });
