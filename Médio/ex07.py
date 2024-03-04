

# QUESTÃO 3892
# "CDISTÂNCIA ENTRE 2 PONTOS"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


cord_x_ponto_A = float(input())
cord_y_ponto_A = float(input())
cord_z_ponto_A = float(input())
cord_x_ponto_B = float(input())
cord_y_ponto_B = float(input())
cord_z_ponto_B = float(input())

dAB = ((cord_x_ponto_B - cord_x_ponto_A)**2 + (cord_y_ponto_B - cord_y_ponto_A)**2 + (cord_z_ponto_B - cord_z_ponto_A)**2)**0.5
print(f'{dAB:.16f}')