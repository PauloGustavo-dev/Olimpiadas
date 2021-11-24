class Ginastica:
  def __init__(self, nome, nota1, nota2, nota3, nota4, nota5, menorNota, totalNotas):
    self.__nome = nome
    self.__nota1 = nota1
    self.__nota2 = nota2
    self.__nota3 = nota3
    self.__nota4 = nota4
    self.__nota5 = nota5
    self.__menorNota = menorNota
    self.__totalNotas = totalNotas

  def getNome(self):
    return self.__nome
  
  def setNome(self, nome):
    self.__nome = nome
  
  def getNota1(self):
    return self.__nota1
  
  def setNota1(self, nota1):
    self.__nota1 = nota1
  
  def getNota2(self):
    return self.__nota2
  
  def setNota2(self, nota2):
    self.__nota2 = nota2
  
  def getNota3(self):
    return self.__nota3
  
  def setNota3(self, nota3):
    self.__nota3 = nota3
  
  def getNota4(self):
    return self.__nota4
  
  def setNota4(self, nota4):
    self.__nota4 = nota4
  
  def getNota5(self):
    return self.__nota5
  
  def setNota5(self, nota5):
    self.__nota5 = nota5

  def getMenorNota(self):
    return self.__menorNota
  
  def setMenorNota(self, menorNota):
    self.__menorNota = menorNota

  def getTotalNotas(self):
    return self.__totalNotas
  
  def setTotalNotas(self, totalNotas):
    self.__totalNotas = totalNotas