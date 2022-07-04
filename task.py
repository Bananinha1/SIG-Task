import calendar
import os
import datetime
os.system('cls') #clear so funcionar no linux, pra windows o comando é cls

anomenu = datetime.datetime.now().year #assim o programa funcionara pra qualquer ano, então é bom trabalhar sempre com datas variaveis

print (f"O calendário do ano {anomenu} é:")
print (calendar.calendar(anomenu))

print('========================= ')
print('        SIG-Task          ')
print('========================= ')
print('  1 - Seleção de usuário  ')
print('  2 - Cadastrar usuário   ')
print('  3 - Alterar usuário     ')
print('  4 - Deletar             ')
print('  0 - Sair                ')
escolha = input('Escolha sua opção: ')

while escolha != "0":
  
  if escolha == "1":
    print("=== Seleção de usuário ===")
    print("=== Em Desenvolvimento ===")
  elif escolha == "2":
    print("=== Cadastro de usuário ===")
    print("=== Em Desenvolvimento ===")
  elif escolha == "3":
    print("===  Alterar usuário   ===")
    print("=== Em Desenvolvimento ===")
  elif escolha == "4":
    print("===   Função Deletar   ===")
    print("=== Em Desenvolvimento ===")
  else:
    print("===   Opção Invalida   ===")
  input("Tecle ENTER para continuar")
  
  os.system('cls') #cls no lugar de clear no windows

  print('========================= ')
  print('        SIG-Task          ')
  print('========================= ')
  print('  1 - Seleção de usuário  ')
  print('  2 - Cadastrar usuário   ')
  print('  3 - Alterar usuário     ')
  print('  4 - Deletar             ')
  print('  0 - Sair                ')
  escolha = input ('Insira: ')
print("Fim")
