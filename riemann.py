# Sumatoria de Riemann
#
# Datos de entrada:
# 1. Función
# 2. Limite inferior
# 3. Límite superior
# 4. Número de rectángulos
#
# Regresar el área bajo la curva.

def main():
    # Leer de entrdada estándar la función
    fn: str = input("Ingrese la función a evaluar: ")

    # Leer de entrada estándar el límite inferior
    Li: float = float(input("Ingrese el límite inferior: "))

    # Leer de entrada estándar el límite superior
    Ls: float = float(input("Ingrese el límite superior: "))

    # Leer de entrada estándar el número de rectángulos
    rc: int = int(input("Ingrese el número de rectángulos: "))

    # Calcular el ancho de los rectángulos. Esto es la resta de los límites
    # dividido entre el número de rectángulos.
    ancho: float = (Ls - Li) / rc

    # Calcular la altura de cada rectángulo. Esto es la evaluación de la función
    # en el punto medio del rectángulo.
    x: float = Li + (ancho / 2)

    # Inicializar el área en 0
    area: float = 0.0

    # Iterar sobre el número de rectángulos
    for _ in range(rc):
        evaluacion: float = eval(fn)
        area += (ancho * evaluacion)
        x: float = x + ancho


    print("El área bajo la curva es: ", area)


if __name__ == '__main__':
    main()
