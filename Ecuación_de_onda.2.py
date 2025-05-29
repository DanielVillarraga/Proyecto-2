import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy.fft import fft, ifft  # Alternativa más estable

# --- Parámetros ---
L = 10.0            #Longitud del dominio espacial
T = 10.0            #Tiempo total de simulación
c = 1.0             #Velocidad de propagación
Nx = 256            #Numero de Puntos
Nt = 100            #Numero de pasos de tiempo
dx = L / Nx         #Resolución espacial
dt = T / Nt         #Resolución temporal
x = np.linspace(0, L, Nx, endpoint=False)       #Malla espacial

# --- Condición inicial ---
def initial_condition(x):
    return np.exp(-(x - L/2)**2 / 0.5)

u0 = initial_condition(x)
v0 = np.zeros(Nx)

# --- Espacio de Fourier ---
k = 2 * np.pi * np.fft.fftfreq(Nx, d=L/Nx)
omega = c * k
omega[0] = 1e-10  # Evita división por cero

# --- Solución espectral ---
def solve_wave_equation_spectral(u0, v0, k, c, dt, Nt):
    """Resuelve la ecuación de onda usando método espectral.
    
    Args:
        u0: Condición inicial de desplazamiento.
        v0: Condición inicial de velocidad.
        k: Vector de frecuencias en espacio de Fourier.
        c: Velocidad de la onda.
        dt: Paso de tiempo.
        Nt: Número de pasos de tiempo.
    
    Returns:
        Lista con la solución en cada paso de tiempo.
    """
    u_hat = fft(u0)
    v_hat = fft(v0)
    solutions = [u0.copy()]
    
    for _ in range(1, Nt):
        t = _ * dt
        u_hat_t = u_hat * np.cos(omega * t) + (v_hat / omega) * np.sin(omega * t)
        u_t = np.real(ifft(u_hat_t))
        solutions.append(u_t.copy())
    
    return solutions

solutions = solve_wave_equation_spectral(u0, v0, k, c, dt, Nt)

# --- Animación ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, L)
ax.set_ylim(-1.1, 1.1)
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return (line,)

def update(frame):
    line.set_data(x, solutions[frame])
    ax.set_title(f'Tiempo: {frame * dt:.2f} s')
    return (line,)

ani = animation.FuncAnimation(
    fig, update, frames=Nt, init_func=init, blit=True, interval=50
)

plt.xlabel('Posición (x)')
plt.ylabel('Amplitud (u)')
plt.grid()
plt.show()

# ani.save('onda_espectral.gif', writer='pillow', fps=20)