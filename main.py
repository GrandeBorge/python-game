class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic


e = Entity(5, 5, "X")

class World:

  def __init__(self, map_x, map_y):

    self.map_x = map_x
    self.map_y = map_y

  def draw(self, *n):

    a = 0
    for y in range(self.map_y):

      for x in range(self.map_x):

        for e in n:

          if e.y-1 == y:
            if e.x-1 == x:
              print("[{}]".format(e.graphic), end = "")
              a = 1
        if a == 0:
          print("[ ]", end="")
        else: 
          a = 0
          
      print()

