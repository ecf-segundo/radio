import locale
import os
import csv
from subprocess import Popen, PIPE, DEVNULL
from dialog import Dialog

def main():
    # Cria dicionario de Radios
    dic_Radios = biblioteca()

    # Definiçoes do Dialog 
    d = Dialog(dialog="dialog")
    # Define o Title 
    d.set_background_title("Radio Player in Python")

    # Criar a variavel "Choices" que é uma lista com as chaves e os valores do dicionário dic_Radios
    Choices = []
    for aux1, aux2 in dic_Radios.items():
       Choices.append(aux1)
       Choices.append(aux2)


    # Executa o Menu
    try:
        # A Variavel "tag" recebe a escolha da rádio (Key)
        code, tag = d.menu("Escolha uma das estações de radio abaixo:",
                            choices=[Choices]
                            )
        # Botão "Aceitar"
        if code == d.OK:
            if tag in dic_Radios.keys():
                url = dic_Radios[tag]
            else:
                print("Radio não existe, verefique o nome digitado")
        try:    
            p = Popen(["mplayer", "-quiet", url], stdout=PIPE, stderr=DEVNULL)
            d.progressbox(text="\n Utilize * ou / para aumentar ou diminuir o volume \n Tocando agora: " + tag,
                               fd=p.stdout.fileno(),
                               title="Playing... " + tag)
        except:
            print("Error code:1")
            pass
    except:
        print("Error code:2")
    d.clear()


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


# Chamada do main
if __name__ == "__main__":
    main()


