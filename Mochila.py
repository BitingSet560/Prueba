import random

# Función para generar números pseudoaleatorios entre 1 y k
def generar_numeros_aleatorios(n, k):
    return [random.randint(1, k) for _ in range(n)]

# Función para resolver el problema de la mochila con fuerza bruta
def mochila_fuerza_bruta(n, capacidad, pesos, valores):
    def knapsack_recursive(i, capacidad_actual):
        if i == 0 or capacidad_actual == 0:
            return 0
        if pesos[i - 1] > capacidad_actual:
            return knapsack_recursive(i - 1, capacidad_actual)
        else:
            sin_incluir = knapsack_recursive(i - 1, capacidad_actual)
            incluyendo = valores[i - 1] + knapsack_recursive(i - 1, capacidad_actual - pesos[i - 1])
            return max(sin_incluir, incluyendo)

    return knapsack_recursive(n, capacidad)

# Parámetros para la generación de números aleatorios y el problema de la mochila
n = 10  # Cantidad de elementos
k = 20  # Intervalo para números aleatorios (1-k)
capacidad_mochila = 50

# Generar números pseudoaleatorios para pesos y valores
pesos = generar_numeros_aleatorios(n, k)
valores = generar_numeros_aleatorios(n, k)

# Resolver el problema de la mochila
valor_optimo = mochila_fuerza_bruta(n, capacidad_mochila, pesos, valores)

print("Pesos de los elementos:", pesos)
print("Valores de los elementos:", valores)
print("Capacidad de la mochila:", capacidad_mochila)
print("Valor óptimo en la mochila:", valor_optimo)
