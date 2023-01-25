import locale
import os
import csv
import sqlite3
from subprocess import Popen, PIPE, DEVNULL
from dialog import Dialog

def main():

<<<<<<< HEAD
    # Banco de Dados SQlite3
    db = sqlite3.connect('radio.db')
    cursor = db.cursor()

=======
>>>>>>> 0d20f5c7b0358a2e9f81416e9011fb2a2f39a8e9
    # Definiçoes do Dialog 
    d = Dialog(dialog="dialog")
    # Define o Title 
    d.set_background_title("Radio Player in Python")

    # Executa o Menu
    try:
        # A Variavel "tag" recebe a escolha
        code, tag = d.menu("Como deseja executar?",
                            choices=[("1", "Utilizar as ultimas estações selecionadas"),
<<<<<<< HEAD
                                     ("2", "Escolher estações ativas"),
                                     ("3", "Busca por novas estações")]
=======
                                     ("2", "Escolher estações")]
>>>>>>> 0d20f5c7b0358a2e9f81416e9011fb2a2f39a8e9
                            )
        # Opcao do primeiro menu
        if code == d.OK:
            # Executa o Player
            if tag == "1":
                try:
<<<<<<< HEAD
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
=======
                    Rplayer(d)
                except:
                    print("Player Error")
            elif tag == "2":
                try:
                    Select_Stations(d)
                except:
                    print("Select Station Error")
>>>>>>> 0d20f5c7b0358a2e9f81416e9011fb2a2f39a8e9
            else:
                print("Nova opção")

        else:
            print("Operação cancelada")
    except:
        print("Error code: 1 - Menu")
<<<<<<< HEAD

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

=======
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
>>>>>>> 0d20f5c7b0358a2e9f81416e9011fb2a2f39a8e9

    # A Variavel "tag" recebe a escolha da rádio (Key)
    code, tag = d.menu("Escolha uma das estações de radio abaixo:",
                        choices=[Choices]
                        )
    # Botão "Aceitar"
    if code == d.OK:
<<<<<<< HEAD
        if tag in Choices:
            url = Choices[Choices.index(tag) + 1]
=======
        if tag in dic_Radios.keys():
            url = dic_Radios[tag]
>>>>>>> 0d20f5c7b0358a2e9f81416e9011fb2a2f39a8e9
        else:
            print("Radio não existe, verefique o nome digitado")
        
        # Executa Mplayer
        p = Popen(["mplayer", "-quiet", url], stdout=PIPE, stderr=DEVNULL)
        d.progressbox(text="\n Utilize * ou / para aumentar ou diminuir o volume \n Tocando agora: " + tag,
<<<<<<< HEAD
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


=======
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

>>>>>>> 0d20f5c7b0358a2e9f81416e9011fb2a2f39a8e9
# Chamada do main
if __name__ == "__main__":
    main()


