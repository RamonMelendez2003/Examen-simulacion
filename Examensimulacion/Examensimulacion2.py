# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:52:11 2025

@author: jean_
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest

# Generador Fibonacci retardado (simplificado)
def lagged_fibonacci(seed, n):
    numbers = list(seed)
    for i in range(len(seed), n):
        next_num = (numbers[i-1] + numbers[i-2]) % 1  # Suma y normaliza
        numbers.append(next_num)
    return numbers

# Prueba de Kolmogorov-Smirnov (más fácil para muestras pequeñas)
def kolmogorov_smirnov_test(numbers):
    result = kstest(numbers, 'uniform')
    return result

# Semilla inicial (debe tener al menos 2 valores)
seed = [0.1, 0.5]
n = 100  # Total de números a generar

# Generar números pseudoaleatorios
random_numbers = lagged_fibonacci(seed, n)

# Mostrar primeros 10 números
print("Primeros 10 números generados:")
for num in random_numbers[:10]:
    print(f"{num:.6f}")

# Prueba Kolmogorov-Smirnov
ks_result = kolmogorov_smirnov_test(random_numbers)

# Resultados
print("\n--- Prueba de Kolmogorov-Smirnov ---")
print(f"Estadístico D: {ks_result.statistic:.4f}")
print(f"Valor p: {ks_result.pvalue:.4f}")
print(f"¿Son uniformes (p > 0.05)? {'Sí' if ks_result.pvalue > 0.05 else 'No'}")

# Gráfica
plt.figure(figsize=(10, 4))
plt.plot(random_numbers, 'o-', markersize=4)
plt.title("Números generados con Fibonacci retardado")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid(True)
plt.show()