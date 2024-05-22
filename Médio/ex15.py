

# QUESTÃO 807
# "Tradução de texto"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


qtd = input()

traducao = {}
for i in range(int(qtd)):
    en, pt = input().split(' => ')
    traducao[en] = pt

while True:   
    string = input()
    if string == '*':
        break

    resp = ''
    for palavra in string.split():
        for i, u in traducao.items():
            if palavra == i:
                resp += u + ' '  
                break  
    print(resp.rstrip()) 

    