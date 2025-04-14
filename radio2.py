from os import system
from pyradios import RadioBrowser

# Dicionário de Dados
def biblioteca(option):
    if option == '':
        Bool = False
        print('Buscador de Radio Onine')
        radio = input('Entre com o nome da Radio a ser buscada:  ')
    else:
        Bool = True
        radio = option
    
    # rs -> radio search
    if radio == '':
        print("Saindo")
        quit()
    rs = RadioBrowser()
    station = rs.search(name=radio, name_exact=Bool)
    return station

# Cria Menu
def menu(station):
    print()
    print('--- MENU Radio ---')
    print()
    n_station = range(len(station))
    print("0- Sair")
    for n in n_station:
        print(str(n+1)+ "- " + station[n]['name'])
    option_num = input('Entre com o número da radio: ')
    if option_num == "0":
        print("Saindo")
        quit()
    option = station[int(option_num)-1]['name']
    return option

# Função Main
def main():
    option = ''
    station = biblioteca(option)
    option = menu(station)
    station = biblioteca(option)
    url = station[0]['url']
    print(url)
    system("cvlc " + url)
    

# Chamada do main
if __name__ == "__main__":
    main()




