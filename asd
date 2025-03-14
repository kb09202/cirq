import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la cohérence
t = np.linspace(0, 10, 500)  # Temps
gamma = 0.1  # Facteur de décohérence

# Simulation d'une fonction de cohérence
def coherence_function(t, gamma):
    return np.exp(-gamma * t) * np.cos(2 * np.pi * t)

coherence = coherence_function(t, gamma)

# Visualisation
plt.plot(t, coherence)
plt.title("Simulation de la cohérence quantique dans les neurones")
plt.xlabel("Temps (ps)")
plt.ylabel("Amplitude de cohérence")
plt.grid()
plt.show()
