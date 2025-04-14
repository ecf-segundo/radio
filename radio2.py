from os import system
from pyradios import RadioBrowser

# Data Dictionary
def biblioteca(option):
    if option == '':
        Bool = False
        print('Radio Onine Search')
        radio = input('Enter the name of Radio to be search:  ')
    else:
        Bool = True
        radio = option
    
    # rs -> radio search
    if radio == '':
        print("Exiting...")
        quit()
    elif radio.lower() == 'spotify':
        station = "spotify"
    else:
        rs = RadioBrowser()
        station = rs.search(name=radio, name_exact=Bool)
    return station

# Create Menu
def menu(station):
    print()
    print('--- MENU Radio ---')
    print()
    n_station = range(len(station))
    print("0- Exit")
    for n in n_station:
        print(str(n+1)+ "- " + station[n]['name'])
    option_num = input('Enter the number of radio: ')
    if option_num == "0":
        print("Exiting...")
        quit()
    option = station[int(option_num)-1]['name']
    return option

# Main Function
def main():
    option = ''
    station = biblioteca(option)
    if station == 'spotify':
        print("Open Spotify")
        system("spotify")
    else:
        option = menu(station)
        station = biblioteca(option)
        url = station[0]['url']
        print(url)
        system("cvlc " + url)
    

# Chamada do main
if __name__ == "__main__":
    main()


