import csv
import os

# Cria o Dicionário de Dados
def biblioteca():
    radios = {}
    # Abre arquivo e percorre linha a linha
    filename="radio.txt"
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            radios[row[0]] = row[1]
    return radios

# Cria Menu
def menu(dic_Radios):
    print('--- MENU Radio ---')
    print()
    for radio in dic_Radios.keys():
        print("- " + radio)
    opcao = input('Entre com o nome da radio: ')
    return opcao

# Função Main
def main():
    dic_Radios = biblioteca()
    escolha = menu(dic_Radios)
    if escolha in dic_Radios.keys():
        url = dic_Radios[escolha]
    else:
        print("Radio não existe, verefique o nome digitado")
    os.system("mplayer " + url)
    

# Chamada do main
if __name__ == "__main__":
    main()




