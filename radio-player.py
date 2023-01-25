import locale
import os
import csv
import sqlite3
from subprocess import Popen, PIPE, DEVNULL
from dialog import Dialog

def main():

    # Banco de Dados SQlite3
    db = sqlite3.connect('radio.db')
    cursor = db.cursor()

    # Definiçoes do Dialog 
    d = Dialog(dialog="dialog")
    # Define o Title 
    d.set_background_title("Radio Player in Python")

    # Executa o Menu
    try:
        # A Variavel "tag" recebe a escolha
        code, tag = d.menu("Como deseja executar?",
                            choices=[("1", "Utilizar as ultimas estações selecionadas"),
                                     ("2", "Escolher estações ativas"),
                                     ("3", "Busca por novas estações")]
                            )
        # Opcao do primeiro menu
        if code == d.OK:
            # Executa o Player
            if tag == "1":
                try:
                    Rplayer(d, cursor)
                except:
                    print("Player Error")
            # Seleção de estaçoes para o Player
            elif tag == "2":
                try:
                    Select_Stations(d, cursor)
                except:
                    print("Select Station Error")
            # Busca e atualização do banco com estaçoes de radio web
            elif tag == "3":
                try:
                    Search_Stations(d, cursor)
                except:
                    print("Search New Station Error")
            else:
                print("Nova opção")

        else:
            print("Operação cancelada")
    except:
        print("Error code: 1 - Menu")

    # Encerra conexão com o banco de dados
    db.commit()
    db.close()
#    d.clear()


#Player das estações
def Rplayer(d, cursor):
    # Carega dicionario de Radios
    cursor.execute("SELECT name, url FROM stations WHERE status = 1")

    # Criar a variavel "Choices" que é uma lista com as chaves e os valores do banco
    Choices = []
    for item in cursor.fetchall():
        Choices.append(item[0])
        Choices.append(item[1])


    # A Variavel "tag" recebe a escolha da rádio (Key)
    code, tag = d.menu("Escolha uma das estações de radio abaixo:",
                        choices=[Choices]
                        )
    # Botão "Aceitar"
    if code == d.OK:
        if tag in Choices:
            url = Choices[Choices.index(tag) + 1]
        else:
            print("Radio não existe, verefique o nome digitado")
        
        # Executa Mplayer
        p = Popen(["mplayer", "-quiet", url], stdout=PIPE, stderr=DEVNULL)
        d.progressbox(text="\n Utilize * ou / para aumentar ou diminuir o volume \n Tocando agora: " + tag,
                            fd=p.stdout.fileno(),
                            title="Playing... " + tag)

    cursor.close()    
    return True

def Select_Stations(d, cursor):
    # Carega dicionario de Radios
    cursor.execute("SELECT name, status FROM stations")

    # Criar a variavel "Choices" que é uma lista com as chaves e os valores do banco
    Choices = []
    for item in cursor.fetchall():
        Choices.append((item[0], "", item[1]))

    # A Variavel "tag" recebe a escolha da rádio (Key)
    code, tag = d.checklist("Escolha uma das estações de radio abaixo:",
                             choices=Choices,
                             title="Seleção das estações da radios",
                             backtitle="Seleção das estações das estaçoes de radios disponíveis")

    # Botão "Aceitar"
    if code == d.OK:
        cursor.execute("SELECT name, id, status FROM stations")
        all_radios = cursor.fetchall()
        for item in all_radios:
            if item[0] in tag:
                # Atualiza o Banco com o campos Status True
                cursor.execute("UPDATE stations SET status = 1 WHERE id = ?", (item[1],))
                cursor.fetchall()
            else:
                # Atualiza o Banco com o campos Status False
                cursor.execute("UPDATE stations SET status = 0 WHERE id = ?", (item[1],))
                cursor.fetchall()
        d.msgbox("Estações Atualizadas")

    cursor.close()    
    return True

def Search_Stations(d, cursor):
    # Carega dicionario de Radios
    cursor.execute("SELECT name, status FROM stations")

#    # Criar a variavel "Choices" que é uma lista com as chaves e os valores do banco
#    Choices = []
#    for item in cursor.fetchall():
#        Choices.append((item[0], "", item[1]))
#
#
#    # A Variavel "tag" recebe a escolha da rádio (Key)
#    code, tag = d.checklist("Escolha uma das estações de radio abaixo:",
#                             choices=Choices,
#                             title="Seleção das estações da radios",
#                             backtitle="Seleção das estações das estaçoes de radios disponíveis")
#
#    # Botão "Aceitar"
#    if code == d.OK:
#        cursor.execute("SELECT name, id, status FROM stations")
#        all_radios = cursor.fetchall()
#        for item in all_radios:
#            if item[0] in tag:
#                # Atualiza o Banco com o campos Status True
#                cursor.execute("UPDATE stations SET status = 1 WHERE id = ?", (item[1],))
#                cursor.fetchall()
#            else:
#                # Atualiza o Banco com o campos Status False
#                cursor.execute("UPDATE stations SET status = 0 WHERE id = ?", (item[1],))
#                cursor.fetchall()
#        d.msgbox("Estações Atualizadas")
#
    cursor.close()    
    return True


# Chamada do main
if __name__ == "__main__":
    main()


