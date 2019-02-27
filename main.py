class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic


e = Entity(5, 5, "X")

class World:
  def draw(lenght,height):
    for x in range(lenght):
      for y in range(height):
        if e.x == x and e.y == y:
          print("[{}]".format(e.graphic), end="")
        else:    
          print("[ ]", end="")
      print()

l = int(input("Definisci la lunghezza del campo > "))
h = int(input("Definisci l'altezza del campo > "))

World.draw(l,h)
       
     

