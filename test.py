class Persona():
  def __init__(self, nome, cognome, anni):
    self.nome = nome
    self.cognome = cognome
    self.anni = anni

  def __str__(self):
    return "{} {} {}".format(self.nome, self.cognome, self.anni)

  def __int__(self):
    return self.anni

p = Persona("Giovanni", "Bruno", 31)
p2 = Persona("Tizio", "Caio", 30)
p3 = p2

if p.anni > p2.anni:
  print(p)