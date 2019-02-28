class Entity:

  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic

e = Entity(5, 9, "X")

class World:

  def __init__(self, map_x, map_y):
    self.map_x = map_x
    self.map_y = map_y

  def draw(self, *n):
    for y in range(self.map_y):
      for x in range(self.map_x):
        for e in n:
          if (e.x - 1 == x) and (e.y - 1) == y:
            print("[{}]".format(e.graphic), end = "")
            break
        else:
          print("[ ]", end = "")

      print()