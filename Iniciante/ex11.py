

# QUESTÃO 385
# "Analisando o CRE"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


turma = {}
media = []

media_baixa = None
nota_baixa = float('inf')  

while True:
    matricula = input()
    if matricula == "999":
        break
        
    nota = float(input())
    media.append(nota)
    turma[matricula] = nota
   
    if nota < nota_baixa:
        nota_baixa = nota
        media_baixa = matricula
        
print(media_baixa)
print(f'{sum(media)/len(media):.2f}')
