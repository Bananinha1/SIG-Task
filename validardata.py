import datetime
import os

from matplotlib.ft2font import HORIZONTAL


def inserirdata():

    valida = False

    while not(valida):

        dia = int(input("Por favor insira o dia: "))
        mes = int(input("Por favor insira o mês: "))
        ano = int(input("Por favor insira o ano: "))

        anoc = ano % 4
        anob = ano % 100
        anod = ano % 400

        if mes > 12 or ano == 0 or mes == 0 or dia == 0:

            print("Data invalida")

        else:
            if mes == 2:

                if (anoc == 0) and (anob != 0) or (anod != 0):

                    bi = 0

                elif (anoc == 0) and (anob != 0) or (anod == 0):

                    bi = 1

            elif (dia >= 32) and ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):

                print("seu dia inserido é invalido pois seu mês so tem 31 dias")

            elif (dia >= 31) and ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)):

                print("seu dia inserido é invalido pois seu mês so tem 30 dias")

            elif (dia == 29) and (mes == 2) and (bi == 0):

                print("seu dia inserido é invalido pois seu mês so tem 28 dias")

            elif (dia == 30) and (mes == 2) and (bi == 1):

                print(
                    "seu dia inserido é invalido pois apesar de ser ano bissexto fevereiro so tem 29 dias")

            else:

                vld = evalido(dia, mes, ano)

                if vld == True:

                    print("Data valida")
                    datavalida = f"{dia}/{mes}/{ano}"
                    print(datavalida)
                    valida = True

    return datavalida


def evalido(dia, mes, ano):
    dt = datetime.datetime.now()
    if ano == dt.year:
        if mes == dt.month:
            if dia >= dt.day:
                return True
        elif mes > dt.month:
            return True
        else:
            return False
    elif ano > dt.year:
        return True
    else:
        return False


# a função que corre os proximos sete dias pra ser usado no modulo 3 pras notificações

def proxsemana(qt):

    data = datetime.datetime.today()
    datat = data.strftime('%d/%m/%Y')
    lista_datas = []
    lista_datas.append(datat)
    for i in range(1, qt):

        data = data + datetime.timedelta(days=1)
        datat = data.strftime('%d/%m/%Y')
        lista_datas.append(datat)

    return lista_datas


def inserirhora(datavalida):

    valida = False

    while not(valida):

        print("Insira o horário do seu evento")
        hora = str(input(" Insira o horario nesse formato(00:00): "))
        horad = datetime.datetime.strptime(hora, '%H:%M')
        horas = horad.hour
        minutos = hord.minute

        if horas > 23 or minutos > 59:

            print("Horario invalido")

        else:

            datah = datetime.datetime.now()
            datahoje = datah.strftime('%d/%m/%Y')

            if datahoje == datavalida:

                diah = hrvalida(horas, minutos)

                if diah == True:
                    valida = True
            else: 
                valida = True

    return hora


def hrvalida(horas, minutos):

    dt = datetime.datetime.now()

    if horas == dt.hour:
        if minutos > dt.minute:
            return True
        else:
            return False
    elif horas > dt.hour:
        return True
    else:
        return False
