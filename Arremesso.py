class Arremesso:
  def __init__(self, nome, arremesso1, arremesso2, arremesso3, maiorArremesso, segundoMaior, menorArremesso):
    self.__nome = nome
    self.__arremesso1 = arremesso1
    self.__arremesso2 = arremesso2
    self.__arremesso3 = arremesso3
    self.__maiorArremesso = maiorArremesso
    self.__segundoMaiorArremesso = segundoMaior
    self.__menorArremesso = menorArremesso

  def getNome(self):
    return self.__nome
  
  def setNome(self, nome):
    self.__nome = nome
  
  def getArremesso1(self):
    return self.__arremesso1
  
  def setArremesso1(self, arremesso1):
    self.__arremesso1 = arremesso1
  
  def getArremesso2(self):
    return self.__arremesso2
  
  def setArremesso2(self, arremesso2):
    self.__arremesso2 = arremesso2
  
  def getArremesso3(self):
    return self.__arremesso3
  
  def setarremesso3(self, arremesso3):
    self.__arremesso3 = arremesso3

  def getMaiorArremesso(self):
    return self.__maiorArremesso
  
  def setmaiorArremesso(self, maiorArremesso):
    self.__maiorArremesso = maiorArremesso

  def getSegundoMaior(self):
    return self.__segundoMaior
  
  def setsegundoMaior(self, segundoMaior):
    self.__segundoMaior = segundoMaior
  
  def getMenorArremesso(self):
    return self.__menorArremesso
  
  def setmenorArremesso(self, menorArremesso):
    self.__menorArremesso = menorArremesso

  