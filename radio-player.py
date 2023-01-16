import locale
import os
import csv
import sqlite3
from subprocess import Popen, PIPE, DEVNULL
from dialog import Dialog

def main():

    # Definiçoes do Dialog 
    d = Dialog(dialog="dialog")
    # Define o Title 
    d.set_background_title("Radio Player in Python")

    # Executa o Menu
    try:
        # A Variavel "tag" recebe a escolha
        code, tag = d.menu("Como deseja executar?",
                            choices=[("1", "Utilizar as ultimas estações selecionadas"),
                                     ("2", "Escolher estações")]
                            )
        # Opcao do primeiro menu
        if code == d.OK:
            # Executa o Player
            if tag == "1":
                try:
                    Rplayer(d)
                except:
                    print("Player Error")
            elif tag == "2":
                try:
                    Select_Stations(d)
                except:
                    print("Select Station Error")
            else:
                print("Nova opção")

        else:
            print("Operação cancelada")
    except:
        print("Error code: 1 - Menu")
#    d.clear()


# Cria o Dicionário de Dados
def biblioteca(radiofile):
    radios = {}
    # Abre arquivo e percorre linha a linha
    filename = radiofile
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            radios[row[0]] = row[1]
    return radios

#Player das estações
def Rplayer(d):
    # Carega dicionario de Radios
    dic_Radios = biblioteca("radio.txt")
       
    # Criar a variavel "Choices" que é uma lista com as chaves e os valores do dicionário dic_Radios
    Choices = []
    for aux1, aux2 in dic_Radios.items():
        Choices.append(aux1)
        Choices.append(aux2)

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
        
        # Executa Mplayer
        p = Popen(["mplayer", "-quiet", url], stdout=PIPE, stderr=DEVNULL)
        d.progressbox(text="\n Utilize * ou / para aumentar ou diminuir o volume \n Tocando agora: " + tag,
                        fd=p.stdout.fileno(),
                        title="Playing... " + tag)
    return True

def Select_Stations(d):
    # Carega dicionario de Estações de Radios Possiveis
    dic_Radios = biblioteca("radio_list.txt")

    # Criar a variavel "Choices" que é uma lista com as chaves e os valores do dicionário dic_Radios
    Choices = []
    for aux1, aux2 in dic_Radios.items():
        Choices.append(aux1)
        Choices.append(aux2)
#        Choices.append(False)

    print("Até aqui")
    print(Choices)
    # A Variavel "tag" recebe a escolha da rádio (Key)
    code, tag = d.menu("Escolha uma das estações de radio abaixo:",
                        choices=[Choices.value],
                        title="Seleção das estações da radios",
                        backtitle="Seleção das estações das estaçoes de radios disponíveis")

    # Botão "Aceitar"
    if code == d.OK:
        print("OK")
#        if tag in dic_Radios.keys():
#            url = dic_Radios[tag]
#        else:
#            print("Radio não existe, verefique o nome digitado")
        
    return True

# Chamada do main
if __name__ == "__main__":
    main()


