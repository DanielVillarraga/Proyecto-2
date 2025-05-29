import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parámetros de la simulación
fil = 1000  # Número de pasos de tiempo
col = 20    # Número de puntos espaciales
L = 2       # Longitud de la cuerda
T = 100     # Tiempo total
c = 0.1     # Velocidad de la onda

# Calculamos los incrementos temporales y espaciales
ht = T/(fil-1)
hx = L/(col-1)
print("(c*ht/hx)**2 =", (c*ht/hx)**2)

# Inicializamos la matriz de solución
M = np.zeros((fil, col))

# Condición inicial
x = np.linspace(0, L, col)
M[0, :] = np.exp(np.pi*x/L)
M[1, :] = M[0, :]

# Resolvemos la ecuación de onda
for n in range(1, fil-1):
    for m in range(1, col-1):
        M[n+1, m] = 2*M[n, m] - M[n-1, m] + (c*ht/hx)**2*(M[n, m+1] - 2*M[n, m] + M[n, m-1])

# Configuración de la figura para la animación
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim((0, L))
ax.set_ylim((-1.1, 1.1))
line, = ax.plot([], [], lw=3, color="red")
ax.set_title("Evolución de la ecuación de onda", size=20)
ax.set_xlabel("Posición en la cuerda", size=15)
ax.set_ylabel("Amplitud", size=15)
ax.grid(True)

# Función de inicialización
def init():
    line.set_data([], [])
    return (line,)

# Función de actualización para cada fotograma
def update(frame):
    line.set_data(x, M[frame, :])
    ax.set_title(f"Evolución de la ecuación de onda - Tiempo: {frame*ht:.2f}", size=20)
    return (line,)

# Creamos la animación
ani = FuncAnimation(
    fig, 
    update, 
    frames=range(0, fil, 10),  # Mostramos cada 10 frames para hacerlo más rápido
    init_func=init, 
    blit=True,
    interval=50,  # 50 ms entre frames
    repeat=False
)

ani.save('onda_animacion.gif', writer='pillow', fps=20)
