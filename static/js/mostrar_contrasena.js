function toggleContrasena() {
    var contrasenaInput = document.getElementById("contrasenaInput");
    var toggleContrasenaBtn = document.getElementById("toggleContrasenaBtn");

    if (contrasenaInput.type === "password") {
        contrasenaInput.type = "text";
        toggleContrasenaBtn.textContent = "Ocultar";
    } else {
        contrasenaInput.type = "password";
        toggleContrasenaBtn.textContent = "Mostrar";
    }
}
function Repetir_contrasena() {
    var contrasenaInput = document.getElementById("Repetir_contrasenaInput");
    var toggleContrasenaBtn = document.getElementById("Repetir_toggleContrasenaBtn");

    if (contrasenaInput.type === "password") {
        contrasenaInput.type = "text";
        toggleContrasenaBtn.textContent = "Ocultar";
    } else {
        contrasenaInput.type = "password";
        toggleContrasenaBtn.textContent = "Mostrar";
    }
}