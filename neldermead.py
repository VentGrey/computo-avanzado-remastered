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

def nelder_mead(f, n, alpha, sigma, delta, rho):
    # Inicializar el simplex.
    x: List[List[float]] = [[random() for _ in range(n)] for _ in range(n + 1)]

    # Mientras no se cumpla la condición de parada.
    while True:
        # Ordenar la población del simplex usando f como llave de ordenación.
        x.sort(key=f)

        # Calcular el centro de masa. Determinar el centro de masa de los n mejores puntos.
        x_cent = [sum([x[i][j] for i in range(n)]) / n for j in range(n)]

        # Calcular la reflexión. (Reflejar el peor punto en el centro de masa).
        x_refl = [x_cent[i] + alpha * (x_cent[i] - x[-1][i]) for i in range(n)]

        # Si la reflexión es mejor que el mejor punto, pero no mejor que el segundo mejor.
        # (Expandir el simplex en la dirección de la reflexión).
        if f(x_refl) < f(x[0]) and f(x_refl) >= f(x[1]):
            x[-1] = x_refl
            continue

        # Si la reflexión es mejor que el mejor punto.
        # (Expandir el simplex en la dirección de la reflexión).
        if f(x_refl) < f(x[0]):
            x_exp = [x_cent[i] + sigma * (x_refl[i] - x_cent[i]) for i in range(n)]
            if f(x_exp) < f(x_refl):
                x[-1] = x_exp
            else:
                x[-1] = x_refl
            continue
