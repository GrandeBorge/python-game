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

class Move:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def move(self, direction):
    while direction != "A" or "S" or "D" or "W" or "a" or "s" or "w" or "d":
      direction = input("Inserisci W, A, S o D")
    if direction == "A" or "a":
      self.y -= 1
    elif direction == "d" or "D":
      self.y += 1
    elif direction == "w" or "W":
      self.x -= 1
    elif direction == "s" or "S":
      self.x += 1

  class Player:
  def __init__(self, x, y, health, damage):
    self.x = x
    self.y = y
    self.health = health
    self.damage = damage
  def damage():
    pass