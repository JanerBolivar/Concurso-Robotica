function mostrarNombreArchivo(numeroBanner) {
    var input = document.getElementById(`inputGroupFile0${numeroBanner}`);
    var label = document.querySelector(`.custom-file-label[for=inputGroupFile0${numeroBanner}]`);
    var nombreArchivo = input.files[0].name;
    label.textContent = nombreArchivo;
}