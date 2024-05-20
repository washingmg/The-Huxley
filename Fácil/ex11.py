

# QUESTÃO 502
# "Agência de Publicidade"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


total = 0
for i in range(7):
    tipo = input()
    if tipo == "Revista":
        total += 750
    elif tipo == "Outdoor":
        total += 1500
    elif tipo == "Rádio":
        emissora = input()
        if emissora == "AM":
            total += 300
        elif emissora == "FM":
            total += 500
    elif tipo == "TV":
        horario = int(input())
        if 20 <= horario <= 23:
            total += 1200
        elif 0 <= horario < 20:
            total += 2000

print('{:.2f}'.format(total))

# Versão do the huxley não aceita o match case.

# total = 0
# for i in range(7):
#     tipo = input()
#     match tipo:
#         case "Revista":
#             total += 750
#         case "Outdoor":
#             total += 1500
#         case "Rádio":
#             emissora = input()
#             if emissora == "AM":
#                 total += 300
#             if emissora == "FM":
#                 total += 500
#         case "TV":
#             horario = int(input())
#             if 20 <= horario <= 23:
#                 total += 1200
#             if horario < 20:
#                 total += 2000

# print('{:.2f}'.format(total))

