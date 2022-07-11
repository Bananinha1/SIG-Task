import calendar
import os
import datetime
import pickle
import agendatype

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
    esc2 = input('Escolha sua opção: ')
    return esc3