

# QUESTÃO 3127
# "Altura máxima - movimento oblíquo"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


import math

def altura_maxima(theta, v, g):
    theta = math.radians(theta)
    h = (v ** 2 * math.sin(theta) ** 2) / (2 * g)
    print(h)


theta = float(input())
v = float(input())
g = float(input())
altura_maxima(theta, v, g)
