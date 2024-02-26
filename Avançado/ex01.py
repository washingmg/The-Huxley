

# QUESTÃO 3885
# "CARTESIANO PARA POLAR"
# NÍVEL DE ACORDO COM O THE HUXLEY: AVANÇADO


import math

x, y = float(input()), float(input())

theta = math.atan(x/y)

r = math.hypot(x, y)

print(r)
print(theta)
