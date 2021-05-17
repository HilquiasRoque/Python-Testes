# Gerador de Nomes Monstruosos : Um programa simples que gera nomes monstruosos a partir de um
#                                nome fornecido pelo usuário com diferenciação entre sexo masculino e feminino
# Autor: Hilquias Roque
# Data: 16/05/2021

from random import randint

monstro = [['Devorador', 'Esmagador', 'Estripador', 'Defecador', 'Vomitador', 'Esganador', 'Empalador', 'Cuspidor',
            'Destruidor', 'Alisador'],
           ['Grotesc', 'Violent', 'Nojent', 'Fei', 'Lepros', 'Estranh', 'Desgraçad', 'Abestalhad', 'Ridícul', 'Tímid'],
           ['de Pôneis', 'de Sapos', 'de Lombrigas', 'de Lixo', 'de Fezes', 'de Cera de Ouvido', 'de Uvas Passas',
            'de Dinheiro', 'de Filhotinhos', 'de Cabelos']]

# Acima uma lista com todas as possibilidades de nomes para combinação. Temos 3 listas dentro de 1 lista.

print(26 * '-=')
print('Quer saber qual é o seu nome monstruoso?')
print('Responda as perguntas abaixo e descubra!')
print(26 * '-=')

print('Qual seu sexo?')
while True:
    sexo = str(input('[M/F]: ')).strip().upper()
    if sexo not in 'MF':  # Validação do sexo permitindo apenas entradas válidas.
        print(26 * '-=')
        print('Escolha uma opção válida.')
    else:
        break

print(26 * '-=')
print('Agora qual o seu nome completo.')

while True:
    nome_real = str(input('(Ex.: Ana da Silva): ')).strip().lower().split(' ')  # Entrada do nome com tratamento direto
    nome_seed = ''.join(nome_real)  # Conversão do nome em uma str sem espaços entre as palavras
    if nome_seed.isalpha() and len(nome_seed) >= 10:  # Validação de comprimento mínimo
        break  # do nome e se contém apenas letras
    else:
        print(26 * '-=')
        print('Digite seu nome completo corretamente.')

valor1 = randint(0, (len(nome_seed) // 3))  # Gerando um número com base no comprimento do nome para usar como
                                            # índice para buscar um nome na lista monstro
valor2 = randint(0, valor1 + 2)   # Gerando outro número com propósito semelhante ao anterior

valor3 = 0
for c in range(0, valor2):  # Mais um número gerado
    valor3 = randint(0, 9)
    c += 1

if sexo == 'M':
    print(26 * '-=')
    print('Seu nome monstruoso é:')
    print(f'{monstro[0][valor1]} {monstro[1][valor2]}{"o"} {monstro[2][valor3]}')
    print(26 * '-=')
else:
    print(26 * '-=')
    print('Seu nome monstruoso é:')
    print(f'{monstro[0][valor1]}{"a"} {monstro[1][valor2]}{"a"} {monstro[2][valor3]}')
    print(26 * '-=')
