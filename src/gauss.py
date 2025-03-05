import numpy as np
import matplotlib.pyplot as plt

# Función gaussiana: A controla la amplitud
def gaussian(x, A=1):
    return A * np.exp(-x**2)

# Derivada de la función gaussiana
def gaussian_derivative(x, A=1):
    return -2 * x * gaussian(x, A)

# Generación de datos para el eje x
x = np.linspace(-3, 3, 400)
y = gaussian(x)
dy = gaussian_derivative(x)

# Configuración y visualización de la gráfica
plt.figure(figsize=(10, 6))

# Cambiar el estilo y color de las líneas
plt.plot(x, y, label='Gaussiana', color='darkblue', linewidth=2, linestyle='-')
plt.plot(x, dy, label='Derivada de Gaussiana', color='crimson', linewidth=2, linestyle=':')

# Añadir relleno bajo las curvas
plt.fill_between(x, y, 0, where=(y >= 0), color='darkblue', alpha=0.3)
plt.fill_between(x, dy, 0, where=(dy >= 0), color='crimson', alpha=0.3)

# Personalizar líneas de los ejes
plt.axhline(0, color='gray', linewidth=1, linestyle='--')
plt.axvline(0, color='gray', linewidth=1, linestyle='--')

# Cambiar el título y etiquetas
plt.title("Función Gaussiana y su Derivada (Con Relleno)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Valor", fontsize=12)

# Añadir leyenda y cuadrícula
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
