

# QUESTÃO 144
# "Álbum"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


x, y = map(int,input().split())
a, b = map(int,input().split())
c, d = map(int,input().split())

area = x * y
foto1 = a * b
foto2 = c * d
if (foto1 + foto2) <= area:
    print('S')
else:
    print('N')