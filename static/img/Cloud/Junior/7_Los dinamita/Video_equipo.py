from dearpygui.core import *
from dearpygui.simple import *
from scipy.optimize import linprog

def resolver_simplex(sender, data):
    # Obtener los valores ingresados por el usuario
    c_values = [float(get_value(f"Coeficiente {i+1}")) for i in range(3)]  # Ejemplo con 3 variables
    b_values = [float(get_value(f"Constante {i+1}")) for i in range(2)]  # Ejemplo con 2 restricciones

    A_values = []
    for i in range(2):  # Ejemplo con 2 restricciones
        row = [float(get_value(f"Restricción {i+1}, Variable {j+1}")) for j in range(3)]  # Ejemplo con 3 variables
        A_values.append(row)

    # Convertir a formato para resolver usando linprog
    c = c_values
    A = A_values
    b = b_values

    # Resolver utilizando el método simplex de SciPy
    resultado = linprog(c, A_ub=A, b_ub=b, method='highs')

    # Mostrar el resultado
    set_value("Resultado", f"Solución óptima:\n{resultado.x}\nValor óptimo: {resultado.fun}")

with window("Calculadora Método Simplex"):
    add_text("Ingrese los coeficientes:")
    for i in range(3):  # Ejemplo con 3 variables
        add_input_float(f"Coeficiente {i+1}")

    add_text("Ingrese las constantes de las restricciones:")
    for i in range(2):  # Ejemplo con 2 restricciones
        add_input_float(f"Constante {i+1}")

    add_text("Ingrese la matriz de restricciones:")
    for i in range(2):  # Ejemplo con 2 restricciones
        with group(f"Restricción {i+1}"):
            for j in range(3):  # Ejemplo con 3 variables
                add_input_float(f"Variable {j+1}")

    add_button("Resolver", callback=resolver_simplex)
    add_text("Resultado:")
    add_text("Resultado", default_value="Aquí aparecerá la solución")

start_dearpygui()
