import numpy as np
import matplotlib.pyplot as plt

# Función escalón: devuelve 1 si x >= 0, de lo contrario 0
def step(x):
    return np.where(x >= 0, 1, 0)

# Derivada de la función escalón: siempre es 0
def step_derivative(x):
    return np.zeros_like(x)

# Generación de datos para el eje x
x = np.linspace(-10, 10, 400)
y = step(x)
dy = step_derivative(x)

# Configuración y visualización de la gráfica
plt.figure(figsize=(10, 6))

# Cambiar el estilo y color de las líneas
plt.plot(x, y, label='Escalón', color='green', linewidth=2, linestyle='-')
plt.plot(x, dy, label='Derivada del Escalón', color='orange', linewidth=2, linestyle=':')

# Añadir relleno bajo la función
plt.fill_between(x, y, 0, where=(y > 0), color='green', alpha=0.2)

# Personalizar líneas de los ejes
plt.axhline(0, color='gray', linewidth=1, linestyle='--')
plt.axvline(0, color='gray', linewidth=1, linestyle='--')

# Cambiar el título y etiquetas
plt.title("Función Escalón y su Derivada (Con Relleno)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Valor", fontsize=12)

# Añadir leyenda y cuadrícula
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
