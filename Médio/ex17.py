

# QUESTÃO 3381
# "Faixa etária idade?"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


def determinar_faixa_etaria(idade):
    faixa_etaria = None
    if idade <= 2:
        faixa_etaria = "O individuo eh um Bebe Jovem Menor de Idade."
    elif idade <= 12:
        faixa_etaria = "O individuo eh uma Crianca Jovem Menor de Idade."
    elif idade < 18:
        faixa_etaria = "O individuo eh um Adolescente Jovem Menor de Idade."
    elif idade <= 19:
        faixa_etaria = "O individuo eh um Jovem Maior de Idade."
    elif 20 <= idade <= 45:
        faixa_etaria = "O individuo eh um Adulto Maior de Idade."
    elif 45 < idade < 60:
        faixa_etaria = "O individuo eh um Adulto de Meia Idade Maior de Idade."
    elif 60 <= idade <= 75:
        faixa_etaria = "O individuo eh um Idoso Maior de Idade."
    elif 75 < idade <= 90:
        faixa_etaria = "O individuo eh um Idoso Ansiao Maior de Idade."
    else:
        faixa_etaria = "O individuo eh um Idoso na Velhice Extrema Maior de Idade."
    
    return faixa_etaria
print(determinar_faixa_etaria(int(input())))