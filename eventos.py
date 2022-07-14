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
                cont += 1
            print('')


def cadevent(nome, tipo):
    os.system('cls')
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
                cont += 1
            print('')


def busdat(nome, tipo):  # inserir print vazio onde tiver o while cont
    dat = validardata.inserirdata()
    for ev in usev[nome]:
        if dat == ev[1] and ev[0] == tipo:
            cont = 1
            while cont < 4:
                print(ev[cont], end=' ')
                cont += 1
            print('')


def listevents(nome, tipo):
    os.system('cls')
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        busnom(nome, tipo)
    elif decid.lower() == 'data':
        busdat(nome, tipo)
    else:
        print('Classificação não encontrada')


def delevents(nome, tipo):
    os.system('cls')
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':

        nomebus = input('Insira o nome: ')
        for events in usev[nome]:
            if nomebus == events[3] and events[0] == tipo:
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                print()
                apg = input("Deseja realmente deletar esse evento?")
                if apg.lower() == 'sim':
                    usev[nome].remove(events)
                    savedic3(usev)
                    print('Evento deletado!')
                else:
                    print()

    elif decid.lower() == 'data':
        databus = input('Insira a data: ')
        for events in usev[nome]:
            if databus == events[1] and events[0] == tipo:
                cont = 1
                while cont < 4:
                    print(events[cont], end=' ')
                    cont += 1
                apg = input("Deseja realmente deletar esse evento?")
                if apg.lower() == 'sim':
                    usev[nome].remove(events)
                    savedic3(usev)
                    break
                else:
                    print('')
                    break
    else:
        print('Classificação não encontrada')


def attnome(nome, tipo):
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


def attdata(nome, tipo):
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


def attevents(nome, tipo):
    os.system('cls')
    decid = input('Buscar os eventos por data ou nome: ')
    if decid.lower() == 'nome':
        attnome(nome, tipo)
    elif decid.lower() == 'data':
        attdata(nome, tipo)
    else:
        print('Classificação não encontrada')


usev = lerdic3()


def modulo3(nome, tipo):

    esc3 = telaeventos(nome, tipo)

    while esc3 != "0":

        if esc3 == "1":
            listevents(nome, tipo)

        elif esc3 == "2":

            cadevent(nome, tipo)

        elif esc3 == "3":
            attevents(nome, tipo)
        elif esc3 == "4":
            delevents(nome, tipo)
        else:
            print("===   Opção Invalida   ===")

        input("Tecle ENTER para continuar")

        esc3 = telaeventos(nome, tipo)


print("Fim")
