import Arremesso
import Ginastica

ar1 = Arremesso.Arremesso("nome",0,0,0,0,0,0)
ar2 = Arremesso.Arremesso("nome",0,0,0,0,0,0)

g1 = Ginastica.Ginastica("nome",0,0,0,0,0,0,0)
g2 = Ginastica.Ginastica("nome",0,0,0,0,0,0,0)

def jogoArremesso():
  ar1.nome = input("Digite o nome do primeiro arremessador: " )
  ar2.nome = input("Digite o nome do segundo  arremessador: " )
  print("\n")
  ar1.arremesso1 = int(input("Digite a distancia do primeiro arremesso do/a {} em metros(apenas numeros): ".format(ar1.nome)))
  ar1.arremesso2 = int(input("Digite a distancia do segundo  arremesso do/a {} em metros(apenas numeros): ".format(ar1.nome)))
  ar1.arremesso3 = int(input("Digite a distancia do terceiro arremesso do/a {} em metros(apenas numeros): ".format(ar1.nome)))
  print("\n")
  print("Agora é a vez do segundo arremesador: ")
  print("\n")
  ar2.arremesso1 = int(input("Digite a distancia do primeiro arremesso do/a {} em metros(apenas numeros): ".format(ar2.nome)))
  ar2.arremesso2 = int(input("Digite a distancia do segundo  arremesso do/a {} em metros(apenas numeros): ".format(ar2.nome)))
  ar2.arremesso3 = int(input("Digite a distancia do terceiro arremesso do/a {} em metros(apenas numeros): ".format(ar2.nome)))
  
#classificacao de notas do jogador1-------------------------------------------------------------------------------------  
  if(ar1.arremesso1 > ar1.arremesso2 and ar1.arremesso1 > ar1.arremesso3):
    ar1.maiorArremesso = ar1.arremesso1
  elif(ar1.arremesso2 > ar1.arremesso1 and ar1.arremesso2 > ar1.arremesso3):
    ar1.maiorArremesso = ar1.arremesso2
  elif(ar1.arremesso3 > ar1.arremesso1 and ar1.arremesso3 > ar1.arremesso2):
    ar1.maiorArremesso = ar1.arremesso3
  else:
    pass
    
  if(ar1.arremesso1 < ar1.arremesso2 and ar1.arremesso1 < ar1.arremesso3):
    ar1.menorArremesso = ar1.arremesso1
  elif(ar1.arremesso2 < ar1.arremesso1 and ar1.arremesso2 < ar1.arremesso3):
    ar1.menorArremesso = ar1.arremesso2
  elif(ar1.arremesso3 < ar1.arremesso1 and ar1.arremesso3 < ar1.arremesso2):
    ar1.menorArremesso = ar1.arremesso3
  else:
    pass

  if(ar1.arremesso1 == ar1.arremesso2 and ar1.arremesso2 != ar1.arremesso3):
    ar1.maiorArremesso = ar1.arremesso1
    ar1.segundoMaiorArremesso = ar1.arremesso2
  elif(ar1.arremesso1 == ar1.arremesso3 and ar1.arremesso2 != ar1.arremesso3):
    ar1.maiorArremesso = ar1.arremesso1
    ar1.segundoMaiorArremesso = ar1.arremesso3
  elif(ar1.arremesso1 == ar1.arremesso2 and ar1.arremesso2 == ar1.arremesso3):
    ar1.maiorArremesso = ar1.arremesso1
    ar1.segundoMaiorArremesso = ar1.arremesso2
    ar1.menorArremesso = ar1.arremesso3
  elif(ar1.arremesso1 < ar1.maiorArremesso and ar1.arremesso1 > ar1.menorArremesso):
    ar1.segundoMaiorArremesso = ar1.arremesso1
  elif(ar1.arremesso2 < ar1.maiorArremesso and ar1.arremesso2 > ar1.menorArremesso):
    ar1.segundoMaiorArremesso = ar1.arremesso2
  elif(ar1.arremesso3 < ar1.maiorArremesso and ar1.arremesso3 > ar1.menorArremesso):
    ar1.segundoMaiorArremesso = ar1.arremesso3
  else:
    pass

#classificacao de notas do jogador2-------------------------------------------------------------------------------------  
  if(ar2.arremesso1 > ar2.arremesso2 and ar2.arremesso1 > ar2.arremesso3):
    ar2.maiorArremesso = ar2.arremesso1
  elif(ar2.arremesso2 > ar2.arremesso1 and ar2.arremesso2 > ar2.arremesso3):
    ar2.maiorArremesso = ar2.arremesso2
  elif(ar2.arremesso3 > ar2.arremesso1 and ar2.arremesso3 > ar2.arremesso2):
    ar2.maiorArremesso = ar2.arremesso3
  else:
    pass
    
  if(ar2.arremesso1 < ar2.arremesso2 and ar2.arremesso1 < ar2.arremesso3):
    ar2.menorArremesso = ar2.arremesso1
  elif(ar2.arremesso2 < ar2.arremesso1 and ar2.arremesso2 < ar2.arremesso3):
    ar2.menorArremesso = ar2.arremesso2
  elif(ar2.arremesso3 < ar2.arremesso1 and ar2.arremesso3 < ar2.arremesso2):
    ar2.menorArremesso = ar2.arremesso3
  else:
    pass

  if(ar2.arremesso1 == ar2.arremesso2 and ar2.arremesso2 != ar2.arremesso3):
    ar2.maiorArremesso = ar2.arremesso1
    ar2.segundoMaiorArremesso = ar2.arremesso2
  elif(ar2.arremesso1 == ar2.arremesso3 and ar2.arremesso2 != ar2.arremesso3):
    ar2.maiorArremesso = ar2.arremesso1
    ar2.segundoMaiorArremesso = ar2.arremesso3
  elif(ar2.arremesso1 == ar2.arremesso2 and ar2.arremesso2 == ar2.arremesso3):
    ar2.maiorArremesso = ar2.arremesso1
    ar2.segundoMaiorArremesso = ar2.arremesso2
    ar2.menorArremesso = ar2.arremesso3
  elif(ar2.arremesso1 < ar2.maiorArremesso and ar2.arremesso1 > ar2.menorArremesso):
    ar2.segundoMaiorArremesso = ar2.arremesso1
  elif(ar2.arremesso2 < ar2.maiorArremesso and ar2.arremesso2 > ar2.menorArremesso):
    ar2.segundoMaiorArremesso = ar2.arremesso2
  elif(ar2.arremesso3 < ar2.maiorArremesso and ar2.arremesso3 > ar2.menorArremesso):
    ar2.segundoMaiorArremesso = ar2.arremesso3
  else:
    pass
  
#analise do vencedor------------------------------------------------------------------------------------------------------ 
  if(ar1.maiorArremesso > ar2.maiorArremesso):
    print("O vencedor é o/a jogador/a: {} com o arremeso de {} metros".format(ar1.nome, ar1.maiorArremesso))
  elif(ar1.maiorArremesso < ar2.maiorArremesso):
    print("O vencedor é o/a jogador/a: {} com o arremeso de {} metros".format(ar2.nome, ar2.maiorArremesso))
  else:
    pass
  if(ar1.maiorArremesso == ar2.maiorArremesso):
    if(ar1.segundoMaiorArremesso > ar2.segundoMaiorArremesso):
      print("O vencedor é o/a jogador/a: {} com o segundo maior arremeso de {} metros".format(ar1.nome, ar1.segundoMaiorArremesso))
    elif(ar1.segundoMaiorArremesso < ar2.segundoMaiorArremesso):
      print("O vencedor é o/a jogador/a: {} com o segundo maior arremeso de {} metros".format(ar2.nome, ar2.segundoMaiorArremesso))
    elif(ar1.segundoMaiorArremesso == ar2.segundoMaiorArremesso):
      if(ar1.menorArremesso > ar2.menorArremesso):
        print("O vencedor é o/a jogador/a: {} com o terceiro maior arremeso de {} metros".format(ar1.nome, ar1.menorArremesso))
      elif(ar1.menorArremesso < ar2.menorArremesso):
        print("O vencedor é o/a jogador/a: {} com o terceiro maior arremeso de {} metros".format(ar2.nome, ar2.menorArremesso))
      else:
        print("empate!!")
  else:
    pass
  print("\n")
#Ginastica-----------------------------------------------------------------------------------------------------------------------------
def jogoGinastica():
  g1.nome = input("Digite o nome do/a 1º ginasta :")
  g2.nome = input("Digite o nome do/a 2º ginasta :")
  print("\n")
  g1.nota1 = int(input("Digite a 1º nota do/a  {} :".format(g1.nome)))
  g1.nota2 = int(input("Digite a 2º nota do/a  {} :".format(g1.nome)))
  g1.nota3 = int(input("Digite a 3º nota do/a  {} :".format(g1.nome)))
  g1.nota4 = int(input("Digite a 4º nota do/a  {} :".format(g1.nome)))
  g1.nota5 = int(input("Digite a 5º nota do/a  {} :".format(g1.nome)))
  print("\n")
  print("Agora é a vez do/a 2º ginasta: ")
  print("\n")
  g2.nota1 = int(input("Digite a 1º nota do/a  {}  ".format(g2.nome)))
  g2.nota2 = int(input("Digite a 2º nota do/a  {}  ".format(g2.nome)))
  g2.nota3 = int(input("Digite a 3º nota do/a  {}  ".format(g2.nome)))
  g2.nota4 = int(input("Digite a 4º nota do/a  {}  ".format(g2.nome)))
  g2.nota5 = int(input("Digite a 5º nota do/a  {}  ".format(g2.nome)))
  print("\n")

#classificacao de notas ginasta 1-------------------------------------------------------------------------------------  
  if(g1.nota1 < g1.nota2 and g1.nota1 < g1.nota3 and g1.nota1 < g1.nota4 and g1.nota1 < g1.nota5):
    g1.menorNota = g1.nota1
  elif(g1.nota2 < g1.nota1 and g1.nota2 < g1.nota3 and g1.nota2 < g1.nota4 and g1.nota2 < g1.nota5):
    g1.menorNota = g1.nota2
  elif(g1.nota3 < g1.nota1 and g1.nota3 < g1.nota2 and g1.nota3 < g1.nota4 and g1.nota3 < g1.nota5):
    g1.menorNota = g1.nota3
  elif(g1.nota4 < g1.nota1 and g1.nota4 < g1.nota2 and g1.nota4 < g1.nota3 and g1.nota4 < g1.nota5):
    g1.menorNota = g1.nota4
  elif(g1.nota5 < g1.nota1 and g1.nota5 < g1.nota2 and g1.nota5 < g1.nota3 and g1.nota5 < g1.nota4):
    g1.menorNota = g1.nota5
  elif(g1.nota1 == g1.nota2 and g1.nota1 == g1.nota3 and g1.nota1 == g1.nota4 and g1.nota1 == g1.nota5):
    g1.menorNota = g1.nota5
  else:
    pass

  g1.totalNotas = ((g1.nota1 + g1.nota2 + g1.nota3 + g1.nota4 +g1.nota5) - g1.menorNota)
#classificacao de notas ginasta 2-------------------------------------------------------------------------------------  
  if(g2.nota1 < g2.nota2 and g2.nota1 < g2.nota3 and g2.nota1 < g2.nota4 and g2.nota1 < g2.nota5):
    g2.menorNota = g2.nota1
  elif(g2.nota2 < g2.nota1 and g2.nota2 < g2.nota3 and g2.nota2 < g2.nota4 and g2.nota2 < g2.nota5):
    g2.menorNota = g2.nota2
  elif(g2.nota3 < g2.nota1 and g2.nota3 < g2.nota2 and g2.nota3 < g2.nota4 and g2.nota3 < g2.nota5):
    g2.menorNota = g2.nota3
  elif(g2.nota4 < g2.nota1 and g2.nota4 < g2.nota2 and g2.nota4 < g2.nota3 and g2.nota4 < g2.nota5):
    g2.menorNota = g2.nota4
  elif(g2.nota5 < g2.nota1 and g2.nota5 < g2.nota2 and g2.nota5 < g2.nota3 and g2.nota5 < g2.nota4):
    g2.menorNota = g2.nota5
  elif(g2.nota1 == g2.nota2 and g2.nota1 == g2.nota3 and g2.nota1 == g2.nota4 and g2.nota1 == g2.nota5):
    g2.menorNota = g2.nota5
  else:
    pass

  g2.totalNotas = ((g2.nota1 + g2.nota2 + g2.nota3 + g2.nota4 +g2.nota5) - g2.menorNota) 
#analise do vencedor------------------------------------------------------------------------------------------------------ 
  if(g1.totalNotas > g2.totalNotas):
    print("O/A vencedor/a é o/a : {} com o total de notas: {}".format(g1.nome, g1.totalNotas))
  elif(g1.totalNotas < g2.totalNotas):
    print("O/A vencedor/a é o/a : {} com o total de notas: {}".format(g2.nome, g2.totalNotas))
  else:
    print("Empate!!")

  print("\n")