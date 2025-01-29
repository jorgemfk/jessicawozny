document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
        let titleJessica = document.getElementById("title-jessica");
        titleJessica.style.opacity = "1";
        titleJessica.style.transform = "translateX(0%)";

        setTimeout(() => {
            let titleWozny = document.getElementById("title-wozny");
            titleWozny.style.opacity = "1";
            titleWozny.style.transform = "translateX(0%)";
        }, 1000); // Aparece 1s después
    }, 500);
});
