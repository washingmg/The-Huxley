

# QUESTÃO 3511
# "É triânuglo é?"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


a,b,c = map(int,input().split())

if (a + b < c) or (a + c < b) or (b + c < a):
    print('nao eh triangulo')
elif (a == b) and (a == c) :
    print('eh equilatero')
elif (a==b) or (a==c) or (b==c):
    print('eh isosceles')
else:
    print('eh escaleno')