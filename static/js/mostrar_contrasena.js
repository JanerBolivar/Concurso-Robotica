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