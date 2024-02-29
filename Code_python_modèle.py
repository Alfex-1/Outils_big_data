import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Définition du système d'équations différentielles
def model(y, t, beta, gamma, alpha):
    S, I, R = y
    dSdt = -beta * S * I * np.exp(-gamma*t)
    dIdt = beta * S * I * np.exp(-gamma*t) - alpha * I
    dRdt = alpha * I
    return [dSdt, dIdt, dRdt]

# Paramètres du modèle
N = 1000  # Nombre total de nœuds dans le réseau
beta = 0.3  # Taux de transmission de l'information
gamma = 0.1  # Taux de récupération (vitesse d'adoption)
alpha = 0.05  # Taux de validation

# Conditions initiales
S0 = N - 1
I0 = 1
R0 = 0

# Temps
t = np.linspace(0, 100, 100)  # De 0 à 100 unités de temps

# Résolution des équations différentielles
result = odeint(model, [S0, I0, R0], t, args=(beta, gamma, alpha))

# Affichage des résultats
plt.plot(t, result[:, 0], label='Susceptibles')
plt.plot(t, result[:, 1], label='Infectés')
plt.plot(t, result[:, 2], label='Récupérés')
plt.xlabel('Temps')
plt.ylabel('Nombre de nœuds')
plt.legend()
plt.show()