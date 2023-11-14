function mostrarNombreArchivo(numeroBanner) {
    var input = document.getElementById(`inputGroupFile0${numeroBanner}`);
    var label = document.querySelector(`.custom-file-label[for=inputGroupFile0${numeroBanner}]`);
    var nombreArchivo = input.files[0].name;
    label.textContent = nombreArchivo;
}

document.addEventListener('DOMContentLoaded', function () {
    var categorias = [];

    document.getElementById('agregarCategoriaBtn').addEventListener('click', function () {
        // Establecer manualmente los valores del formulario en blanco
        document.getElementById('nombreCategoria').value = '';
        document.getElementById('descripcionCategoria').value = '';
        document.getElementById('valorCategoria').value = '';
        document.getElementById('reglasCategoria').innerHTML = ''; // Limpiar las reglas al abrir la ventana modal

        $('#modalCategoria').modal('show'); // Mostrar la ventana modal al agregar categoría
    });

    document.getElementById('guardarCategoriaBtn').addEventListener('click', function () {
        var nombreCategoria = document.getElementById('nombreCategoria').value;
        var descripcionCategoria = document.getElementById('descripcionCategoria').value;
        var valorCategoria = document.getElementById('valorCategoria').value;

        if (nombreCategoria && descripcionCategoria && valorCategoria) {
            var reglas = obtenerReglas(); // Obtener las reglas ingresadas

            categorias.push({
                nombre: nombreCategoria,
                descripcion: descripcionCategoria,
                valor: valorCategoria,
                reglas: reglas
            });

            actualizarTarjetasCategorias();

            $('#modalCategoria').modal('hide');
        } else {
            alert('Por favor, complete todos los campos.');
        }
    });

    function obtenerReglas() {
        var reglas = [];
        var inputsReglas = document.querySelectorAll('.reglaInput');

        inputsReglas.forEach(function (input) {
            var nombreRegla = input.querySelector('.nombreRegla').value;
            var descripcionRegla = input.querySelector('.descripcionRegla').value;

            if (nombreRegla && descripcionRegla) {
                reglas.push({
                    nombre: nombreRegla,
                    descripcion: descripcionRegla
                });
            }
        });

        return reglas;
    }

    document.getElementById('agregarReglaBtn').addEventListener('click', function () {
        // Crear dinámicamente los elementos de entrada para una nueva regla
        var divRegla = document.createElement('div');
        divRegla.className = 'form-group reglaInput';

        divRegla.innerHTML = `
            <label for="nombreRegla">Nombre de la regla</label>
            <input type="text" class="form-control nombreRegla" required />
            <label for="descripcionRegla">Descripción de la regla</label>
            <textarea class="form-control descripcionRegla" rows="2" required></textarea>
            <hr/>
        `;

        document.getElementById('reglasCategoria').appendChild(divRegla);
    });

    function actualizarTarjetasCategorias() {
        var categoriasContainer = document.getElementById('categoriasContainer');

        categoriasContainer.innerHTML = '';

        categorias.forEach(function (categoria, index) {
            var nuevaTarjeta = document.createElement('div');
            nuevaTarjeta.className = 'col-sm-6 p-3';
            nuevaTarjeta.innerHTML = `
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title" id="nombre_categoria_card_${index}">${categoria.nombre}</h5>
                        <p class="card-text" id="descripcion_categoria_card_${index}">${categoria.descripcion} - Valor: ${categoria.valor}</p>
                        <button class="btn btn-primary" onclick="mostrarInformacionCategoria(${index})">Saber más</button>
                    </div>
                </div>
            `;
            categoriasContainer.appendChild(nuevaTarjeta);
        });
    }

    // Función para mostrar la información completa de una categoría, incluyendo todas las reglas
    window.mostrarInformacionCategoria = function (index) {
        var categoria = categorias[index];

        var informacionCategoria = `
            <h4>${categoria.nombre}</h4>
            <p>${categoria.descripcion} - Valor: ${categoria.valor}</p>
            <h5>Reglas:</h5>
        `;

        categoria.reglas.forEach(function (regla) {
            informacionCategoria += `<p>${regla.nombre}: ${regla.descripcion}</p>`;
        });

        // Crear una ventana emergente para mostrar la información
        var ventanaEmergente = window.open('', 'InformacionCategoria', 'width=600,height=400,scrollbars=yes,resizable=yes');
        ventanaEmergente.document.body.innerHTML = informacionCategoria;
    };
});
