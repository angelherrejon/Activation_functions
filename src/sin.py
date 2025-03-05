import numpy as np
import matplotlib.pyplot as plt

# Función sinusoidal
def sinusoidal(x, A=1, omega=1, phi=0):
    return A * np.sin(omega * x + phi)

# Derivada de la función sinusoidal
def sinusoidal_derivative(x, A=1, omega=1, phi=0):
    return A * omega * np.cos(omega * x + phi)

# Generación de datos para el eje x
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = sinusoidal(x)
dy = sinusoidal_derivative(x)

# Configuración y visualización de la gráfica
plt.figure(figsize=(10, 6))

# Cambiar el estilo y color de las líneas
plt.plot(x, y, label='Sinusoidal', color='blue', linewidth=2, linestyle='-.')
plt.plot(x, dy, label='Derivada', color='green', linewidth=2, linestyle=':')

# Rellenar entre la función y el eje x
plt.fill_between(x, y, 0, where=(y >= 0), color='blue', alpha=0.1)
plt.fill_between(x, y, 0, where=(y < 0), color='blue', alpha=0.1)
plt.fill_between(x, dy, 0, where=(dy >= 0), color='green', alpha=0.1)
plt.fill_between(x, dy, 0, where=(dy < 0), color='green', alpha=0.1)

# Personalizar líneas de los ejes
plt.axhline(0, color='gray', linewidth=1, linestyle='--')
plt.axvline(0, color='gray', linewidth=1, linestyle='--')

# Cambiar el título y etiquetas
plt.title("Función Sinusoidal y su Derivada (Con Relleno)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Valor", fontsize=12)

# Añadir leyenda y cuadrícula
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
