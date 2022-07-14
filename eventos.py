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


def cadevent(tipo, nome):
    print("Vamos cadastrar um novo evento")
    data = validardata.inserirdata()
    hora = validardata.inserirhora(data)
    nomeev = input("Insira o nome do evento: ")
    listaevento = [tipo, data, hora, nomeev]
    usev[nome].append(listaevento)
    savedic3(usev)
    print("Cadastro Efetuado")


def busnom(nome):
    nomebus = input('Insira o nome: ')
    for events in usev[nome]:
        if nomebus == events[3]:
            nome = events
            return (nome)


def busdat(data):
    dat = inserirdata(data)
    for ev in usev[data]:
        if dat == ev[1]:
            date = ev
            return (date)


def listevents(nome, data):
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        busnom(nome)
        print(nome)
    elif decid.lower() == 'data':
        busdat(data)
        print(date)
    else:
        decid = input('Classificação não encontrada, insira novamente: ')


def deleve(nome, data):
    decid = input('Buscar os eventos por data ou nome:')
    if decid.lower() == 'nome':
        busnom(nome)
        if nome in usev:
            del usev[nome]
    elif decid.lower() == 'data':
        busnom(data)
        if date in usev:
            del usev[date]
    else:
        decid = input('Classificação não encontrada, insira novamente: ')
    savedic3(usev)


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
