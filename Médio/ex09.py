

# QUESTÃO 4137
# "ÁREA DE FIGURAS"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


import math

def calcularArea(formato, lado):

  if lado <= 0:
    return None  

  area = None
  if formato in ('C', 'c'):
    area = math.pi * lado**2
  elif formato in ('Q', 'q'):
    area = lado**2
  elif formato in ('T', 't'):
    area = (lado**2 * 1.7) / 4
  else:
    return None
  
  return area

formato = input()
lado = float(input())

area = calcularArea(formato, lado)

if area is None:
  print("Entrada invalida!")
else:
  print(f"{area:.2f}")  
  if formato in ('C', 'c'):
    print("Circulo")
  elif formato in ('Q', 'q'):
    print("Quadrado")
  elif formato in ('T', 't'):
    print("Triangulo equilatero")
