import numpy as np
import matplotlib.pyplot as plt  

# Importación de funciones de activación y transformaciones
from src.sig import sigmoid
from src.escalon import step
from src.gauss import gaussian
from src.identidad import identity
from src.linea_tramos import piecewise
from src.ReLu import relu
from src.sin import sinusoidal
from src.tanh import tanh

def plot_functions():
    x = np.linspace(-10, 10, 400)  # Genera los puntos para el eje x
    
    # Evaluamos cada función para los valores de x
    y = {
        'Sigmoide': sigmoid(x),
        'Escalón': step(x),
        'Gaussiana': gaussian(x),
        'Identidad': identity(x),
        'Lineal a Tramos': piecewise(x),
        'ReLU': relu(x),
        'Sinusoidal': sinusoidal(x),
        'Tangente Hiperbólica': tanh(x)
    }
    
    # Colores para cada gráfico
    colors = ['blue', 'green', 'purple', 'red', 'orange', 'cyan', 'magenta', 'brown']
    
    fig, axs = plt.subplots(4, 2, figsize=(12, 12))  # Configuramos la figura con subgráficas
    axs = axs.flatten()  # Convertimos la matriz de ejes a una lista para facilitar el acceso
    
    # Graficamos cada función y asignamos el título correspondiente
    for i, (func_name, values) in enumerate(y.items()):
        axs[i].plot(x, values, color=colors[i], linewidth=2)  # Color y grosor de línea
        axs[i].fill_between(x, values, color=colors[i], alpha=0.1)  # Sombreado debajo de la curva
        axs[i].set_title(func_name, fontsize=12, fontweight='bold')  # Título con estilo
        axs[i].grid(True, linestyle='--', alpha=0.6)  # Añadimos una cuadrícula estilizada
    
    plt.tight_layout()  # Ajusta el diseño para evitar superposiciones
    plt.show()  # Muestra todos los gráficos

# Ejecuta la función principal si el script es llamado directamente
if __name__ == "__main__":
    plot_functions()
