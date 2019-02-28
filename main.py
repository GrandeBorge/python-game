class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic


e = Entity(5, 5, "X")

for y in range(10):
  for x in range(10):
    if e.x == x and e.y == y:
      print("[{}]".format(e.graphic), end="")
    else:
      print("[ ]", end="")

  print()

class Player:
  def __init__(self, x, y, health, damage):
    self.x = x
    self.y = y
    self.health = health
    self.damage = damage
  def damage():
    pass