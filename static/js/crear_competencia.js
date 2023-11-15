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
        document.getElementById('reglasCategoria').innerHTML = ''; // Limpiar las reglas al abrir la ventana modal
        document.getElementById('areasEvaluacionContainer').innerHTML = ''; // Limpiar las reglas al abrir la ventana modal

        $('#modalCategoria').modal('show'); // Mostrar la ventana modal al agregar categoría
    });

    document.getElementById('guardarCategoriaBtn').addEventListener('click', function () {
        var nombreCategoria = document.getElementById('nombreCategoria').value;
        var descripcionCategoria = document.getElementById('descripcionCategoria').value;

        if (nombreCategoria && descripcionCategoria) {
            var reglas = obtenerReglas(); // Obtener las reglas ingresadas
            var areasEvaluacion = obtenerAreasEvaluacion(); // Obtener las areas de evaluacion ingresadas

            categorias.push({
                nombre: nombreCategoria,
                descripcion: descripcionCategoria,
                reglas: reglas,
                areasEvaluacion: areasEvaluacion
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

    function obtenerAreasEvaluacion() {
        var areasEvaluacion = [];
        var inputsAreas = document.querySelectorAll('.areaInput');

        inputsAreas.forEach(function (input) {
            var nombreArea = input.querySelector('.nombreArea').value;
            var descripcionArea = input.querySelector('.descripcionArea').value;
            var porcentajeArea = input.querySelector('.porcentajeArea').value;

            if (nombreArea && descripcionArea && porcentajeArea) {
                areasEvaluacion.push({
                    nombre: nombreArea,
                    descripcion: descripcionArea,
                    porcentaje: porcentajeArea
                });
            }
        });

        return areasEvaluacion;
    }

    //Crear reglas
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

    //Crear Area de evaluacion
    document.getElementById('agregarAreaBtn').addEventListener('click', function () {
        // Crear dinámicamente los elementos de entrada para una nueva área de evaluación
        var divArea = document.createElement('div');
        divArea.className = 'form-group areaInput';

        divArea.innerHTML = `
          <label for="nombreArea">Nombre del Área</label>
          <input type="text" class="form-control nombreArea" required />
          <label for="descripcionArea">Descripción del Área</label>
          <textarea class="form-control descripcionArea" rows="2" required></textarea>
          <label for="porcentajeArea">Porcentaje</label>
          <input type="number" class="form-control porcentajeArea" required />
          <hr/>
        `;

        document.getElementById('areasEvaluacionContainer').appendChild(divArea);
    });

    function mostrarInformacionCategoriaModal(categoria) {
        document.getElementById('modalInformacionCategoriaLabel').textContent = categoria.nombre;
        document.getElementById('modalCategoriaDescripcion').textContent = categoria.descripcion;

        var reglasHTML = '';
        categoria.reglas.forEach(function (regla) {
            reglasHTML += `<li>${regla.nombre}: ${regla.descripcion}</li>`;
        });
        document.getElementById('modalCategoriaReglas').innerHTML = reglasHTML;

        var areasEvaluacionHTML = '';
        categoria.areasEvaluacion.forEach(function (area) {
            areasEvaluacionHTML += `<li>${area.nombre}: ${area.descripcion} - Porcentaje: ${area.porcentaje}%</li>`;
            document.getElementById('modalCategoriaAreasEvaluacion').innerHTML = areasEvaluacionHTML;
        });
        document.getElementById('modalCategoriaAreasEvaluacion').innerHTML = areasEvaluacionHTML;

        $('#modalInformacionCategoria').modal('show');
    }

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
                        <p class="card-text" id="descripcion_categoria_card_${index}">${categoria.descripcion}</p>
                        <button class="btn btn-primary mostrar-info" type="button" data-index="${index}">Saber más</button>
                    </div>
                </div>
            `;
            categoriasContainer.appendChild(nuevaTarjeta);
        });

        // Añadir evento click a los botones "Saber más"
        var botonesSaberMas = document.querySelectorAll('.mostrar-info');
        botonesSaberMas.forEach(function (boton) {
            boton.addEventListener('click', function (event) {
                var index = event.target.getAttribute('data-index');
                var categoria = categorias[index];
                mostrarInformacionCategoriaModal(categoria);
            });
        });
    }



    // Resto de tu código...
});
