document.addEventListener("DOMContentLoaded", function () {


    // ==========================================
    // MENÚ PARA CELULARES
    // ==========================================

    const menuToggle = document.getElementById("menuToggle");
    const menu = document.getElementById("menu");

    if (menuToggle && menu) {

        menuToggle.addEventListener("click", function () {

            menu.classList.toggle("menu-abierto");

        });

    }


    // ==========================================
    // VALIDACIÓN DEL REGISTRO
    // ==========================================

    const formulario = document.getElementById("formRegistro");

    if (formulario) {

        formulario.addEventListener("submit", function (event) {

            const password =
                document.getElementById("password").value;

            const passwordConfirm =
                document.getElementById("password_confirm").value;


            // Verificar contraseñas
            if (password !== passwordConfirm) {

                alert("Las contraseñas no coinciden.");

                event.preventDefault();

                return;
            }


            // Mínimo 8 caracteres
            if (password.length < 8) {

                alert(
                    "La contraseña debe tener al menos 8 caracteres."
                );

                event.preventDefault();

                return;
            }


            // Mayúscula
            if (!/[A-Z]/.test(password)) {

                alert(
                    "La contraseña debe contener al menos una letra mayúscula."
                );

                event.preventDefault();

                return;
            }


            // Número
            if (!/[0-9]/.test(password)) {

                alert(
                    "La contraseña debe contener al menos un número."
                );

                event.preventDefault();

                return;
            }

        });

    }


    // ==========================================
    // MOSTRAR / OCULTAR CONTRASEÑA
    // ==========================================

    const mostrarPassword =
        document.getElementById("mostrarPassword");

    if (mostrarPassword) {

        mostrarPassword.addEventListener("click", function () {

            const password =
                document.getElementById("password");

            if (password.type === "password") {

                password.type = "text";

                mostrarPassword.textContent =
                    "🙈 Ocultar contraseña";

            } else {

                password.type = "password";

                mostrarPassword.textContent =
                    "👁️ Mostrar contraseña";

            }

        });

    }


    // ==========================================
    // MOSTRAR / OCULTAR CONFIRMACIÓN
    // ==========================================

    const mostrarPasswordConfirm =
        document.getElementById("mostrarPasswordConfirm");

    if (mostrarPasswordConfirm) {

        mostrarPasswordConfirm.addEventListener("click", function () {

            const passwordConfirm =
                document.getElementById("password_confirm");

            if (passwordConfirm.type === "password") {

                passwordConfirm.type = "text";

                mostrarPasswordConfirm.textContent =
                    "🙈 Ocultar confirmación";

            } else {

                passwordConfirm.type = "password";

                mostrarPasswordConfirm.textContent =
                    "👁️ Mostrar confirmación";

            }

        });

    }

});

// Confirma antes de eliminar una herramienta
function confirmarEliminacion() {

    return confirm(
        "¿Estás seguro de que deseas eliminar esta herramienta ninja?"
    );
}