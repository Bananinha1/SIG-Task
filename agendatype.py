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

def savedic2(ust):
    arq1 = open('ustype.dat', 'wb')
    pickle.dump(ust, arq1)
    arq1.close()

def lerdic2():
    try:
        arq1 = open("ustype.dat", "rb")
        ust = pickle.load(arq1)
        arq1.close()
    except:
        arq1 = open("ustype.dat", "wb")
        arq1.close()

    return ust

def selectipos():
    os.system("cls")
    print("=== Seleção de tipo de Agenda ===\n")

    for tipos in ust:
        print(tipos)
    print()

    wt = input("Informe qual tipo de agenda deseja visualizar ")

    if ust.get(wt):

        print("Função para entrar no proximo crudd")

    else:
        print(f'Agenda do tipo: {wt} não encontrada')

    print("=== Em Desenvolvimento ===")


def cadtipo():
    os.system("cls")
    print("=== Cadastro de novo tipo de agenda ===")
    nome = input('Insira o nome do tipo de agenda: ')

    if ust.get(nome):

        print(f'Agenda do tipo: {nome} já existe')
    else:
        senha = input('Insira sua senha: ')
        us[nome] = senha
        ust[nome] = [] #tipo de agenda, nome do evento, data, hora
        savedic1(us)
        savedic2(ust)
        print("=== Cadastro efetuado ===")

ust = lerdic2()

esc2 = telatipo()

while esc2 != "0":
    if esc2 == "1":

        selectipos()

    elif esc2 == "2":

        print("Em construção!")
    
    elif esc2 == "3":

        print("Em construção!")

    elif esc2 == "4":

        print("Em construção!")

    else:
        print("===   Opção Invalida   ===")

    input("Tecle ENTER para continuar")

    esc2 = telatipo()


