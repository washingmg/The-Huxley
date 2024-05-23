

# QUESTÃO 1053
# "Volume e área de um cilindro"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


altura = float(input())
raio = float(input())

pi = 3.14
print(f'{pi*raio**2 * altura:.2f}')
print(f'{2 * pi * raio * altura + 2* pi * raio**2:.2f}')
