document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("contact-form").addEventListener("submit", function (e) {
        e.preventDefault();
        // Obtener valores de los campos
        let email = document.getElementById("email").value.trim();
        let message = document.getElementById("message").value.trim();

        // Obtener elementos para mostrar errores
        let emailError = document.getElementById("email-error");
        let messageError = document.getElementById("message-error");

        // Expresión regular para validar correo electrónico
        let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // Bandera de validación
        let isValid = true;

        // Validar email
        if (!emailRegex.test(email)) {
            emailError.innerText = "Ingrese un correo electrónico válido.";
            isValid = false;
        } else {
            emailError.innerText = "";
        }

        // Validar mensaje
        if (message.length === 0) {
            messageError.innerText = "El mensaje no puede estar vacío.";
            isValid = false;
        } else if (message.length > 1000) {
            messageError.innerText = "El mensaje no debe exceder los 1000 caracteres.";
            isValid = false;
        } else {
            messageError.innerText = "";
        }

        // Si no pasa la validación, detener el envío
        if (!isValid) {
            return;
        }
        let formData = new FormData(this);

        fetch("/contacto/", {
            method: "POST",
            body: formData,
            /*headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCSRFToken(),
            },*/
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("response-message").innerText = "Mensaje enviado con éxito.";
                setTimeout(closeModal, 2000);
            } else {
                document.getElementById("response-message").innerText = "Error al enviar el mensaje.";
            }
        });
    });
});

// Obtener CSRF Token
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(cookie => {
            let trimmedCookie = cookie.trim();
            if (trimmedCookie.startsWith("csrftoken=")) {
                cookieValue = trimmedCookie.split("=")[1];
            }
        });
    }
    alert(cookieValue);
    return cookieValue;
}

// Mostrar y ocultar el modal
function openModal() {
    document.getElementById("contacto-modal").style.display = "block";
}

function closeModal() {
    document.getElementById("contacto-modal").style.display = "none";
}
