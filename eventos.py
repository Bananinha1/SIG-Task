import calendar
import os
import datetime
import pickle
from typing import Dict, List, NoReturn
import validardata

# modulo 3 vai dar certo demais

# na função de atualizar, verificar se a nova atualização tem um nome de algum evento ja existente

# Na função de deletar: criar variavel booleana e gerar um while, ai quando printar o evento, pergunta se é esse o evento da pessoa, se for ai entre no if da linha 139 senão continua o for e vai mostrando todos os eventos daquela data


def telaeventos(nome, tipo, usev):  # interface do terceiro modulo
    os.system('cls')
    anomenu = datetime.datetime.now().year
    mesmenu = datetime.datetime.now().month

    print(f"O calendário do seu mes {mesmenu} do ano {anomenu} é:")
    print(calendar.month(anomenu, mesmenu))
    print("Seus eventos mais proximos são:")
    notifevents(nome, tipo, usev)
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


def savedic3(usev):  # salvando em dicionario
    arq2 = open('userevent.dat', 'wb')
    pickle.dump(usev, arq2)
    arq2.close()


def lerdic3():  # lendo dicionario
    try:
        arq2 = open("userevent.dat", "rb")
        usev = pickle.load(arq2)
        arq2.close()
    except:
        arq2 = open("userevent.dat", "wb")
        arq2.close()

    return usev


def notifevents(nome, tipo, usev):  # função de notificação de eventos

    for event in usev[nome]:
        dataref = validardata.proxsemana(4)
        if (event[0] == tipo) and (event[1] in dataref):
            cont = 1
            while cont < 4:
                print(event[cont], end=' ')
                cont += 1
            print('')


def cadevent(nome, tipo, usev):  # cadastro de eventos
    os.system('cls')
    print("Vamos cadastrar um novo evento")
    data = validardata.inserirdata()
    hora = validardata.inserirhora(data)
    nomeev = input("Insira o nome do evento: ")
    event_list = []
    for evento in usev[nome]:
        event_list.append(evento[-1])
    print(event_list)
    while True:
        if nomeev in event_list:
            nomeev = input(
                "Nome já cadastro, insira novamente um nome para evento: ")
        else:
            break
    listaevento = [tipo, data, hora, nomeev]
    usev[nome].append(listaevento)
    savedic3(usev)
    print("Cadastro Efetuado")


def busnom(nome, tipo, usev):  # função de buscar por nome
    nomebus = input('Insira o nome: ')
    for events in usev[nome]:
        if nomebus == events[3] and events[0] == tipo:
            cont = 1
            while cont < 4:
                print(events[cont], end=' ')
                cont += 1
            print('')


# inserir print vazio onde tiver o while cont
def busdat(nome: str, tipo: str, usev: Dict[str, List[str]]) -> NoReturn:
    """Buscar por data

    Args:
        nome: nome de user
        tipo: tipo de evento
        usev: dicionario com eventos
    """
    dat = validardata.inserirdata()
    for ev in usev[nome]:
        if dat == ev[1] and ev[0] == tipo:
            cont = 1
            while cont < 4:
                print(ev[cont], end=' ')
                cont += 1
            print('')


def listevents(nome, tipo, usev):  # func de listagem de eventos
    os.system('cls')
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        busnom(nome, tipo, usev)
    elif decid.lower() == 'data':
        busdat(nome, tipo, usev)
    else:
        print('Classificação não encontrada')


def delevents(nome, tipo, usev):  # func de deletar eventos
    os.system('cls')
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        nomebus = input('Insira o nome: ')
        qs = False
        while not qs:
            for events in usev[nome]:
                if nomebus == events[3] and events[0] == tipo:
                    cont = 1
                    while cont < 4:
                        print(events[cont], end=' ')
                        cont += 1
                    print()
                    apg = input("Deseja realmente deletar esse evento?")
                    if apg.lower() == 'sim':
                        qs = True
                    else:
                        print()
        if qs == True:
            usev[nome].remove(events)
            savedic3(usev)
            print()
    elif decid.lower() == 'data':

        # criar variavel booleana e gerar um while, ai quando printar o evento, pergunta se é esse o evento da pessoa, se for ai entre no if da linha 139 senão continua o for e vai mostrando todos os eventos daquela data

        databus = input('Insira a data: ')
        qs = False
        while not qs:
            for events in usev[nome]:
                if databus == events[1] and events[0] == tipo:
                    cont = 1
                    while cont < 4:
                        print(events[cont], end=' ')
                        cont += 1
                    print()
                    ev = input('Esse é seu evento (sim/não)? ')
                    if ev.lower() == 'sim':
                        qs = True
                    else:
                        print()
        if qs == True:
            usev[nome].remove(events)
            savedic3(usev)
            print()
    else:
        print('Classificação não encontrada')


def attnome(nome, tipo, usev):  # func de atualizar nome
    nomebus = input('Insira o nome: ')
    for events in usev[nome]:
        if nomebus == events[3] and events[0] == tipo:
            cont = 1
            while cont < 4:
                print(events[cont], end=' ')
                cont += 1
            print('')
            att = input(
                "Deseja atualizar por nome, data, hora ou o evento completo:\n")
            if att.lower == "nome":
                novonome = input('Insira a mudança de nome: ')
                if novonome in usev:
                    novonome = input(
                        "Nome já cadastro, insira novo nome para evento: ")
                events[3] = novonome
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            elif att.lower == "data":
                novadata = validardata.inserirdata()
                events[1] = novadata
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            elif att.lower == "hora":
                novahora = input('Insira a mudança de hora: ')
                events[2] = novahora
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            elif att.lower == "completo":
                novadata = validardata.inserirdata()
                events[1] = novadata
                novahora = input('Insira a mudança de hora: ')
                events[2] = novahora
                novonome = input('Insira a mudança de nome: ')
                if novonome in usev:
                    novonome = input(
                        "Nome já cadastro, insira novo nome para evento: ")
                events[3] = novonome
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            else:
                print('Classificação não encontrada!')
        else:
            print('Evento não encontrado')


def attdata(nome, tipo, usev):  # func de atualizar data
    databus = input('Insira a data: ')
    for events in usev[nome]:
        if databus == events[1] and events[0] == tipo:
            cont = 1
            while cont < 4:
                print(events[cont], end=' ')
                cont += 1
            att = input(
                "Deseja atualizar por nome, data, hora ou o evento completo:\n")
            if att.lower == "nome":
                novonome = input('Insira a mudança de nome: ')
                events[3] = novonome
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            elif att.lower == "data":
                novadata = validardata.inserirdata()
                events[1] = novadata
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            elif att.lower == "hora":
                novahora = input('Insira a mudança de hora: ')
                events[2] = novahora
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            elif att.lower == "completo":
                novadata = validardata.inserirdata()
                events[1] = novadata
                novahora = input('Insira a mudança de hora: ')
                events[2] = novahora
                novonome = input('Insira a mudança de nome: ')
                events[3] = novonome
                savedic3(usev)
                print('Evento Atualizado')
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print('')
            else:
                print('Classificação não encontrada!')
        else:
            print('Evento não encontrado')


def attevents(nome, tipo, usev):  # func de atualizar eventos
    os.system('cls')
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        attnome(nome, tipo, usev)
    elif decid.lower() == 'data':
        attdata(nome, tipo, usev)
    else:
        print('Classificação não encontrada')


# usev = lerdic3()


def modulo3(nome, tipo, usev):  # módulo 3

    esc3 = telaeventos(nome, tipo, usev)

    while esc3 != "0":

        if esc3 == "1":
            listevents(nome, tipo, usev)

        elif esc3 == "2":

            cadevent(nome, tipo, usev)

        elif esc3 == "3":
            attevents(nome, tipo, usev)
        elif esc3 == "4":
            delevents(nome, tipo, usev)
        else:
            print("===   Opção Invalida   ===")

        input("Tecle ENTER para continuar")

        esc3 = telaeventos(nome, tipo, usev)


print("Fim")
