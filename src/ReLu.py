import numpy as np
import matplotlib.pyplot as plt

# Función ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada de la función ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Generación de datos para el eje x
x = np.linspace(-3, 3, 400)
y = relu(x)
dy = relu_derivative(x)

# Configuración y visualización de la gráfica
plt.figure(figsize=(10, 6))

# Cambiar el estilo y color de las líneas
plt.plot(x, y, label='ReLU', color='orange', linewidth=2, linestyle='-')
plt.plot(x, dy, label='Derivada de ReLU', color='green', linewidth=2, linestyle=':')

# Rellenar entre la función y el eje x
plt.fill_between(x, y, 0, where=(y >= 0), color='orange', alpha=0.2)
plt.fill_between(x, dy, 0, where=(dy >= 0), color='green', alpha=0.2)

# Personalizar líneas de los ejes
plt.axhline(0, color='gray', linewidth=1, linestyle='--')
plt.axvline(0, color='gray', linewidth=1, linestyle='--')

# Cambiar el título y etiquetas
plt.title("Función ReLU y su Derivada (Con Relleno)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Valor", fontsize=12)

# Añadir leyenda y cuadrícula
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
