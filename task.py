import calendar
import os
import datetime
import pickle
import agendatype


def savedic1(us):
    arq = open('users.dat', 'wb')
    pickle.dump(us, arq)
    arq.close()


def savedic3(usev):
    arq2 = open('userevent.dat', 'wb')
    pickle.dump(usev, arq2)
    arq2.close()


def telamenu():
    os.system('cls')
    anomenu = datetime.datetime.now().year
    mesmenu = datetime.datetime.now().month

    print(f"O calendário do seu mes {mesmenu} do ano {anomenu} é:")
    print(calendar.month(anomenu, mesmenu))
    print('========================= ')
    print('        SIG-Task          ')
    print('========================= ')
    print('  1 - Seleção de usuário  ')
    print('  2 - Cadastrar usuário   ')
    print('  3 - Atualizar usuário   ')
    print('  4 - Deletar             ')
    print('  0 - Sair                ')
    esc1 = input('Escolha sua opção: ')
    return esc1


def lerdic1():
    try:
        arq = open("users.dat", "rb")
        us = pickle.load(arq)
        arq.close()
    except:
        arq = open("users.dat", "wb")
        arq.close()

    return us


def selectuser():
    os.system("cls")
    print("=== Seleção de usuário ===\n")

    for users in us:
        print(users)
    print()

    wu = input("Informe com qual Usuario deseja entrar: ")

    if us.get(wu):
        cont = 0
        su = input("Insira a senha: ")

        while su != us[wu] and cont < 5:  # valida a senha
            su = input("Senha incorreta, tente novamente: ")
            cont += 1
        if cont == 5:
            print('Número de tentativas de acesso excedidas')
        elif su == us[wu]:
            print('Usuário %s validado' % wu)
            agendatype.modulo2(wu)

    else:
        print(f'Usuário {wu} não encontrado')

    print("=== Em Desenvolvimento ===")


def caduser():
    os.system("cls")
    print("=== Cadastro de usuário ===")
    nome = input('Insira seu nome: ')

    if us.get(nome):

        print(f'Usuário {nome} já existe')
    else:
        senha = input('Insira sua senha: ')
        us[nome] = senha
        ust[nome] = ["Estudantil", "Profissional", "Pessoal"]
        usev[nome] = []
        savedic1(us)
        savedic2(ust)
        savedic3(usev)
        print("=== Cadastro efetuado ===")


def atuser():
    os.system("cls")
    print("===  Atualizar usuário   =")
    nome = input('Insira o nome usuário a se mudar: ')
    if nome in us:
        crtz = input('Você tem certeza que deseja mudar? ')
        if crtz.lower() in "sim":
            if nome in us.keys():

                nome2 = input('Insira o novo nome: ')
                senha = input('Insira a nova senha: ')
                us[nome2] = senha
                vprov = ust[nome]
                vprov2 = usev[nome]
                ust[nome2] = vprov
                usev[nome2] = vprov2
                del us[nome]
                del ust[nome]
                del usev[nome]
                savedic1(us)
                savedic2(ust)
                savedic3(usev)
                print("=== Usuário Atualizado ===")

        else:

            print("Usuário não foi atualizado!")
    else:
        print("Nome não encontrado!")


def exuser():
    os.system("cls")
    print("===   Função Deletar   ===")
    nome = input('Insira o usuário que será deletado: ')
    if nome in us.keys():
        su = input("Insira a senha: ")
        cont = 0
        while su != us[nome] and cont < 5:  # valida a senha
            su = input("Senha incorreta, tente novamente: ")
            cont += 1
        if cont == 5:
            print('Número de tentativas de acesso excedidas')
        elif su == us[nome]:
            del us[nome]
            del ust[nome]
            del usev[nome]
            savedic2(ust)
            savedic1(us)
            savedic3(usev)
            print("=== Usuário Deletado ===")
    else:
        print("Usuário não encontrado")


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


def lerdic3():
    try:
        arq2 = open("userevent.dat", "rb")
        usev = pickle.load(arq2)
        arq2.close()
    except:
        arq2 = open("userevent.dat", "wb")
        arq2.close()

    return usev


us = lerdic1()

ust = lerdic2()

usev = lerdic3()

esc1 = telamenu()


while esc1 != "0":

    if esc1 == "1":

        selectuser()

    elif esc1 == "2":

        caduser()

    elif esc1 == "3":

        atuser()

    elif esc1 == "4":

        exuser()

    else:
        print("===   Opção Invalida   ===")

    input("Tecle ENTER para continuar")

    esc1 = telamenu()


print("Fim")
