from asyncio import events
import calendar
import os
import datetime
import pickle
import validardata

# modulo 3 vai dar certo demais


def telaeventos(nome, tipo):
    os.system('cls')
    anomenu = datetime.datetime.now().year
    mesmenu = datetime.datetime.now().month

    print(f"O calendário do seu mes {mesmenu} do ano {anomenu} é:")
    print(calendar.month(anomenu, mesmenu))
    print("Seus eventos mais proximos são:")
    notifevents(nome, tipo)
    print('========================= ')
    print('SIG-Task - Agenda de eventos')
    print('========================= ')
    print('  1 - Ver eventos marcados  ')
    print('  2 - Cadastrar  Novo Evento   ')
    print('  3 - Modificar evento   ')
    print('  4 - Deletar Evento             ')
    print('  0 - Sair                ')
    esc3 = input('Escolha sua opção: ')
    return esc3


def savedic3(usev):
    arq2 = open('userevent.dat', 'wb')
    pickle.dump(usev, arq2)
    arq2.close()


def lerdic3():
    try:
        arq2 = open("userevent.dat", "rb")
        usev = pickle.load(arq2)
        arq2.close()
    except:
        arq2 = open("userevent.dat", "wb")
        arq2.close()

    return usev


def notifevents(nome, tipo):

    for event in usev[nome]:
        dataref = validardata.proxsemana(4)
        if (event[0] == tipo) and (event[1] in dataref):
            cont = 1
            while cont < 4:
                print(event[cont], end=' ')


def cadevent(nome, tipo):
    print("Vamos cadastrar um novo evento")
    data = validardata.inserirdata()
    hora = validardata.inserirhora(data)
    nomeev = input("Insira o nome do evento: ")
    listaevento = [tipo, data, hora, nomeev]
    usev[nome].append(listaevento)
    savedic3(usev)
    print("Cadastro Efetuado")


def busnom(nome, tipo):
    nomebus = input('Insira o nome: ')
    for events in usev[nome]:
        if nomebus == events[3] and events[0] == tipo:
            cont = 1
            while cont < 4:
                print(events[cont], end=' ')
            
            

def busdat(nome, tipo):
    dat = validardata.inserirdata()
    for ev in usev[nome]:
        if dat == ev[1] and ev[0] == tipo:
            cont = 1
            while cont < 4:
                print(ev[cont], end=' ')


def listevents(nome, tipo):
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        busnom(nome, tipo)
    elif decid.lower() == 'data':
        busdat(nome, tipo)
    else:
        print('Classificação não encontrada')

def delevents(nome, tipo):
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':

        nomebus = input('Insira o nome: ')
        for events in usev[nome]:
            if nomebus == events[3] and events[0] == tipo:
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                apg = input("Deseja realmente deletar esse evento?")
                if apg.lower() == 'sim':
                    del events
                    savedic3(usev)
                else:
                    print()

    elif decid.lower() == 'data':
        databus = input('Insira o nome: ')
        for events in usev[nome]:
            if databus == events[1] and events[0] == tipo:
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                apg = input("Deseja realmente deletar esse evento?")
                if apg.lower() == 'sim':
                    del events
                    savedic3(usev)
                    break 
                else:
                    print()
                    break
    else:
        print('Classificação não encontrada')


usev = lerdic3()


esc3 = telaeventos()


while esc3 != "0":

    if esc3 == "1":
        listevents()

    elif esc3 == "2":

        cadevent()

    elif esc3 == "3":
        print('b')
    elif esc3 == "4":
        print('a')
    else:
        print("===   Opção Invalida   ===")

    input("Tecle ENTER para continuar")

    esc3 = 0


print("Fim")
