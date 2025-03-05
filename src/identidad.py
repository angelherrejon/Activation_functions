import numpy as np
import matplotlib.pyplot as plt

# Función identidad: devuelve el mismo valor de entrada
def identity(x):
    return x

# Derivada de la función identidad: siempre es 1
def identity_derivative(x):
    return np.ones_like(x)

# Generación de datos para el eje x
x = np.linspace(-10, 10, 400)
y = identity(x)
dy = identity_derivative(x)

# Configuración y visualización de la gráfica
plt.figure(figsize=(10, 6))

# Cambiar el estilo y color de las líneas
plt.plot(x, y, label='Identidad', color='blue', linewidth=2, linestyle='-')
plt.plot(x, dy, label='Derivada de la Identidad', color='red', linewidth=2, linestyle=':')

# Rellenar entre la función y el eje x
plt.fill_between(x, y, 0, where=(y >= 0), color='blue', alpha=0.2)
plt.fill_between(x, dy, 0, where=(dy >= 0), color='red', alpha=0.2)

# Personalizar líneas de los ejes
plt.axhline(0, color='gray', linewidth=1, linestyle='--')
plt.axvline(0, color='gray', linewidth=1, linestyle='--')

# Cambiar el título y etiquetas
plt.title("Función Identidad y su Derivada (Con Relleno)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Valor", fontsize=12)

# Añadir leyenda y cuadrícula
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
