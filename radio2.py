from os import system
from pyradios import RadioBrowser

# Dicionário de Dados
def biblioteca(option):
    if option == '':
        Bool = False
        radio = input('Entre com o nome da Radio a ser buscada:  ')
    else:
        Bool = True
        radio = option
    
    # rs -> radio search
    rs = RadioBrowser()
    station = rs.search(name=radio, name_exact=Bool)
    # SL - Station List
    #SL = stations[0]['name'],stations[0]['url']
    #return SL
    return station

# Cria Menu
def menu(station):
    print('--- MENU Radio ---')
    print()
    n_station = range(len(station))
    for n in n_station:
        print("- " + station[n]['name'])
    option = input('Entre com o nome da radio: ')
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




