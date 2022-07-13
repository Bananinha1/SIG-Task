import calendar
import os
import datetime
import pickle


def telatipo():
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


def savedic2(ust):
    arq1 = open('ustype.dat', 'wb')
    pickle.dump(ust, arq1)
    arq1.close()

# rep


def lerdic2():
    try:
        arq1 = open("ustype.dat", "rb")
        ust = pickle.load(arq1)
        arq1.close()
    except:
        arq1 = open("ustype.dat", "wb")
        arq1.close()

    return ust


def selectipos(nome):
    os.system("cls")
    print("=== Seleção de tipo de Agenda ===\n")

    for tipos in ust[nome]:
        print(tipos)
    print()

    wt = input("Informe qual tipo de agenda deseja visualizar ")

    if wt in ust[nome]:

        print("Função para entrar no proximo crudd")

    else:
        print(f'Agenda do tipo: {wt} não encontrada')

    print("=== Em Desenvolvimento ===")


def cadtipo(nome):
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


def attipo(nome):
    os.system("cls")
    print("===  Atualizar Tipos de Evento   =")
    tipo = input('Insira o tipo de evento a se mudar: ')

    if tipo in ust[nome]:
        crtz = input('Você tem certeza que deseja mudar? ')
        if crtz.lower() in "sim":
            if tipo in ust[nome]:
                vprov = ust[nome]
                vprov.remove(tipo)
                tipon = input(
                    'Insira o nova nomenclatura para esses eventos: ')
                vprov.append(tipon)
                ust[nome] = vprov
                attevs(nome, tipo, tipon)
                savedic2(ust)
                print("=== Tipo de evento Atualizado ===")

        else:

            print("Tipo de evento não foi atualizado!")
    else:
        print("Tipo não encontrado!")


def attipo(nome, tipo, tipon):
    for event in usev[nome]:
        if event[0] == tipo:
            event[0] = tipon
        savedic3(usev)


def deltipo(nome, tipo):
    for event in usev[nome]:
        if event[0] == tipo:
            del event
        savedic3(usev)


def delevs(nome, tipo):
    for event in usev[nome]:
        if event[0] == tipo:
            del event
        savedic3(usev)

# rep


def savedic3(usev):
    arq2 = open('userevent.dat', 'wb')
    pickle.dump(usev, arq2)
    arq2.close()

# rep


def lerdic3():
    try:
        arq2 = open("userevent.dat", "rb")
        usev = pickle.load(arq2)
        arq2.close()
    except:
        arq2 = open("userevent.dat", "wb")
        arq2.close()

    return usev


def deletipo(nome):
    os.system("cls")
    print("===   Função Deletar   ===")
    tipo = input('Insira o tipo a ser deletado: ')
    if tipo in ust[nome]:
        vprov = ust[nome]
        vprov.remove(tipo)
        ust[nome] = vprov
        delevents(nome, tipo)
        savedic2(ust)
        print("=== Tipo Deletado ===")
    else:
        print("Tipo não encontrado")


ust = lerdic2()

usev = lerdic3()


def modulo2(nome):

    esc2 = telatipo()

    while esc2 != "0":
        if esc2 == "1":

            selectipos(nome)

        elif esc2 == "2":

            cadtipo(nome)

        elif esc2 == "3":

            attipo(nome)

        elif esc2 == "4":

            deletipo(nome)

        else:
            print("===   Opção Invalida   ===")

        input("Tecle ENTER para continuar")

        esc2 = telatipo()
