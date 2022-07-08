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
    esc1 = input('Escolha sua opção: ')
    return esc1

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