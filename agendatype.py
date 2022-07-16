import calendar
import os
import datetime
import pickle
import eventos


def telatipo(): #tela do segundo módulo
    os.system('cls')
    anomenu = datetime.datetime.now().year
    mesmenu = datetime.datetime.now().month

    print(f"O calendário do seu mes {mesmenu} do ano {anomenu} é:")
    print(calendar.month(anomenu, mesmenu))
    print('========================= ')
    print('SIG-Task - Tipos de Agenda')
    print('========================= ')
    print('  1 - Seleção de tipo de Agenda  ')
    print('  2 - Cadastrar  Nova Agenda   ')
    print('  3 - Atualizar tipo de Agenda   ')
    print('  4 - Deletar             ')
    print('  0 - Sair                ')
    esc2 = input('Escolha sua opção: ')
    return esc2

# rep


def savedic2(ust): #salvando dicionário de tipo 
    arq1 = open('ustype.dat', 'wb')
    pickle.dump(ust, arq1)
    arq1.close()

# rep


def lerdic2(): #lendo dicionário
    try:
        arq1 = open("ustype.dat", "rb")
        ust = pickle.load(arq1)
        arq1.close()
    except:
        arq1 = open("ustype.dat", "wb")
        arq1.close()

    return ust


def selectipos(nome, ust, usev): #função para selecionar tipo de agenda
    os.system("cls")
    print("=== Seleção de tipo de Agenda ===\n")

    for tipos in ust[nome]:
        print(tipos)
    print()

    wt = input("Informe qual tipo de agenda deseja visualizar ")

    if wt in ust[nome]:
        eventos.modulo3(nome, wt, usev)

    else:
        print(f'Agenda do tipo: {wt} não encontrada')

    print("=== Em Desenvolvimento ===")


def cadtipo(nome, ust): #função de cadastramento de tipo de agenda
    os.system("cls")
    print("=== Cadastro de novo tipo de agenda ===")
    tipo = input('Insira o nome do tipo de agenda: ')

    if tipo in ust[nome]:

        print(f'Agenda do tipo: {tipo} já existe')
    else:
        vprov = ust[nome]
        vprov.append(tipo)
        del ust[nome]
        ust[nome] = vprov
        savedic2(ust)
        print("=== Cadastro efetuado ===")


def attipo(nome, ust, usev): #função de atualizar tipo de agenda
    os.system("cls")
    print("===  Atualizar Tipos de Agenda   =")
    tipo = input('Insira o tipo de evento a se mudar: ')

    if tipo in ust[nome]:
        crtz = input('Você tem certeza que deseja mudar? ')
        if crtz.lower() in "sim":
            if tipo in ust[nome]:
                
                tipon = input('Insira o nova nomenclatura para esses eventos: ')
                if tipon in ust[nome]:
                    print("Nomenclatura já existente")
                    print("Tipo de evento não foi atualizado!")
                else:

                    vprov = ust[nome]
                    vprov.remove(tipo)
                    vprov.append(tipon)
                    ust[nome] = vprov
                    attevs(nome, tipo, tipon, usev)
                    savedic2(ust)
                    # savedic3(usev)
                    print("=== Tipo de evento Atualizado ===")

        else:

            print("Tipo de evento não foi atualizado!")
    else:
        print("Tipo não encontrado!")


def attevs(nome, tipo, tipon, usev): #função de atualizar
    for event in usev[nome]:
        if event[0] == tipo:
            event[0] = tipon
        savedic3(usev)



def delevs(nome, tipo, usev): #função de deletar
    for event in usev[nome]:
        if event[0] == tipo:
            del event
        savedic3(usev)

# rep


def savedic3(usev): #salvando no dicionario de eventos
    arq2 = open('userevent.dat', 'wb')
    pickle.dump(usev, arq2)
    arq2.close()

# rep


def lerdic3(): #lendo dicionario
    try:
        arq2 = open("userevent.dat", "rb")
        usev = pickle.load(arq2)
        arq2.close()
    except:
        arq2 = open("userevent.dat", "wb")
        arq2.close()

    return usev


def deletipo(nome, ust, usev): #deletando tipo de agenda
    os.system("cls")
    print("===   Função Deletar   ===")
    tipo = input('Insira o tipo a ser deletado: ')
    if tipo in ust[nome]:
        vprov = ust[nome]
        vprov.remove(tipo)
        ust[nome] = vprov
        delevs(nome, tipo, usev)
        savedic2(ust)
        print("=== Tipo Deletado ===")
    else:
        print("Tipo não encontrado")


# ust = lerdic2()

# usev = lerdic3()


def modulo2(nome, ust, usev): #módulo 2 em geral

    esc2 = telatipo()

    while esc2 != "0":
        if esc2 == "1":

            selectipos(nome, ust, usev)

        elif esc2 == "2":

            cadtipo(nome, ust)

        elif esc2 == "3":

            attipo(nome, ust, usev)

        elif esc2 == "4":

            deletipo(nome, ust, usev)

        else:
            print("===   Opção Invalida   ===")

        input("Tecle ENTER para continuar")

        esc2 = telatipo()
