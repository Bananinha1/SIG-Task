import calendar
import os
os.system('clear')


print ("O calendário do ano 2022 é:")
print (calendar.calendar(2022))

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
  
  os.system('clear')
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
