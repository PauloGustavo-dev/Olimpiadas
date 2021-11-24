import Mecanicas

print("Ola bem vindo as olimpiadas")

decisor = 0
while(decisor == 0):
  print("-----------------MENU------------------|")
  print("----- Escolha uma das modalidades -----|")
  print("1 - Arremesso de peso                  |")
  print("2 - Ginastica Artistica                |")
  print("3 - Sair                               |")
  print("---------------------------------------|")

  escolha = int(input("Opção Escolhida: "))

  if(escolha == 1):
    Mecanicas.jogoArremesso()

  elif(escolha == 2):
    Mecanicas.jogoGinastica()
        
  elif(escolha == 3):
    decisor = decisor + 1

  else:
    print("Digite um numero valido")
    
