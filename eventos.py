import calendar
import os
import datetime
import pickle

#modulo 3 vai dar certo demais

def telaeventos():
    os.system('cls')
    anomenu = datetime.datetime.now().year
    mesmenu = datetime.datetime.now().month

    print(f"O calendário do seu mes {mesmenu} do ano {anomenu} é:")
    print(calendar.month(anomenu, mesmenu))
    print('========================= ')
    print('SIG-Task - Agenda de eventos')
    print('========================= ')
    print('  1 - Ver eventos futuros  ')
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

def mostevs(nome, tipo):
    
    #do jeito q ta vai funcionar mas vai mostrar todos os eventos          

    #criar uma função que salva os proximos 7 dias em uma lista como strings, e usar a função in para verficar se esta na lista o event{o} pq ai consigo limitar essas notificações so aos proximos 7 dias hehehe 



    for event in usev[nome]:
        if event[0] == tipo:
            cont = 1
            while cont < 4:
                 print(event[cont], end=' ')


        


usev = lerdic3()






