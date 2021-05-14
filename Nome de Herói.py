nomes = [['Super', 'Mega', 'Ultra', 'Hiper', 'Master', 'Giga', 'Abominável', 'Espantoso', 'Esquisito', 'Ridículo'],
         ['Afanador', 'Triturador', 'Destruidor', 'Caçador', 'Aniquilador', 'Socador', 'Demolidor', 'Descascador',
          'Engolidor', 'Devorador'],
         ['das Galáxias', 'das Profundezas', 'do Universo', 'da Vizinhança', 'do Vazio', 'das Feras', 'da Preula',
          'da Peste', 'da Bexiga', 'do Mundo']]
print(f'{22*"-="}-')
print('''|     Digite a sua data de nascimento e     | 
|     descubra seu nome de Super-Herói!     |''')
print(f'{22*"-="}-')
while True:
    datanasc = str(input('Ex.: 31/12/2001: ')).strip()
    datalista = datanasc.split('/')
    datastring = ''.join(datalista)
    if datastring.isnumeric() and len(datastring) == 8:
        break
    else:
        print('Digite no formato válido.')

ndia = int(datastring[1:2])
nmes = int(datastring[3:4])
nano = int(datastring[-1])
print(f'{22*"-="}-')
print("*{:^43}*".format("Seu nome de Herói é:"))
print(f'>>>>> {nomes[0][ndia]} {nomes[1][nmes]} {nomes[2][nano]} <<<<<')
print(f'{22*"-="}-')
