

# QUESTÃO 428
# "Formatando endereço"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


nome_rua = input()
numero_residencia = int(input())
nome_bairro = input()
cidade = input()
estado = input()
cep = int(input())

print(f'{nome_rua}, {numero_residencia}.')
print(f'Bairro: {nome_bairro}. Cep: {cep}')
print(f'{cidade}/{estado}')