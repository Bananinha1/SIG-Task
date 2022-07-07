import calendar
import os
import datetime
import pickle  # biblioteca pra gravar o dicionario inteiro no arquivo


def savedic1(us):
    arq = open('users.dat', 'wb')
    pickle.dump(us, arq)
    arq.close()


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

        su = input("Insira a senha: ")
        while su != us[wu]:  # valida a senha
            su = input("Senha incorreta, tente novamente: ")

        print("Função para entrar no proximo crudd")

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
        savedic1(us)
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
                del us[nome]
                savedic1(us)
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
        while su != us[nome]:  # valida a senha
            su = input("Senha incorreta, tente novamente: ")
        if su == us[nome]:
            del us[nome]
            savedic1(us)
            print("=== Usuário Deletado ===")
    else:
        print("Usuário não encontrado")


us = lerdic1()

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
