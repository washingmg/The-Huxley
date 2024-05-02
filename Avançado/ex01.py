

# QUESTÃO 3885
# "CARTESIANO PARA POLAR"
# NÍVEL DE ACORDO COM O THE HUXLEY: AVANÇADO


import math

x, z = float(input()), float(input())

theta = math.atan(x/z)

r = math.hypot(x, z)

print(r)
print(theta)
