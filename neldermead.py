from random import random
from typing import List

# Algoritmo Nelder-Mead. Sin bibliotecas y Python 100% tipado para extra cáncer.
# Entrada: f que es la funcion objetivo a minimizar
# Entrada: n + 1 que es el número de puntos iniciales en el simplex
# Entrada: alpha, sigma, delta y rho que son los coeficientes de expansión,
# contracción y reducción
# Salida: x que es el punto mínimo de la función objetivo

# Definir una función esfera usando comprehension lists
def sphere(x: List[float]) -> float:
    return sum([xi**2 for xi in x])

def nelder_mead(f, n: int, alpha: int, sigma: int, delta: float, rho: float):
    # Inicializar el simplex.
    x: List[List[float]] = [[random() for _ in range(n)] for _ in range(n + 1)]

    # Mientras no se cumpla la condición de parada.
    while True:
        # Ordenar la población del simplex usando f como llave de ordenación.
        x.sort(key=f)

        # Calcular el centro de masa. Determinar el centro de masa de los n mejores puntos.
        x_cent = [sum([x[i][j] for i in range(n)]) / n for j in range(n)]
        print("-----iteración con centro de masa: ", x_cent, "----------------")
        print("Valor del centro de masa: ", x_cent)

        # Calcular el punto de reflexión.
        x_ref = [x_cent[i] + alpha * (x_cent[i] - x[-1][i]) for i in range(n)]

        print("Valor del punto de reflexión: ", x_ref)

        # Si el punto de reflexión es mejor que el mejor punto del simplex.
        if f(x_ref) < f(x[0]):
            # Calcular el punto de expansión.
            x_exp = [x_cent[i] + sigma * (x_ref[i] - x_cent[i]) for i in range(n)]

            print("Valor del punto de expansión: ", x_exp)

            # Si el punto de expansión es mejor que el punto de reflexión.
            if f(x_exp) < f(x_ref):
                # Reemplazar el peor punto del simplex por el punto de expansión.
                x[-1] = x_exp
            # Si el punto de expansión es peor que el punto de reflexión.
            else:
                # Reemplazar el peor punto del simplex por el punto de reflexión.
                x[-1] = x_ref
        # Si el punto de reflexión es peor que el peor punto del simplex.
        elif f(x_ref) > f(x[-2]):
            # Calcular el punto de contracción.
            x_con = [x_cent[i] + delta * (x[-1][i] - x_cent[i]) for i in range(n)]

            print("Valor del punto de contracción: ", x_con)
            print("-----------------------------------------------------------")
            # Si el punto de contracción es mejor que el peor punto del simplex.
            if f(x_con) < f(x[-1]):
                # Reemplazar el peor punto del simplex por el punto de contracción.
                x[-1] = x_con
            # Si el punto de contracción es peor que el peor punto del simplex.
            else:
                # Reducir el simplex.
                for i in range(1, n + 1):
                    x[i] = [x[0][j] + rho * (x[i][j] - x[0][j]) for j in range(n)]
        # Si el punto de reflexión es mejor que el peor punto del simplex.
        else:
            # Reemplazar el peor punto del simplex por el punto de reflexión.
            x[-1] = x_ref

        # Si la condición de parada se cumple.
        if all([abs(x[-1][i] - x[0][i]) < 1e-6 for i in range(n)]):
            # Devolver el mejor punto del simplex.
            return x[0]

# Ejemplo de uso.
if __name__ == "__main__":
    # Definir la función objetivo.
    f = sphere

    # Definir los parámetros del algoritmo.
    n: int = 2
    alpha: int = 1
    sigma: int = 2
    delta: float = 0.5
    rho: float = 0.5

    # Ejecutar el algoritmo.
    x: List[float] = nelder_mead(f, n, alpha, sigma, delta, rho)

    # Imprimir el resultado.
    print("El punto mínimo es: ", x)
