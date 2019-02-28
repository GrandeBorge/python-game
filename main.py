class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic
class Mobile(Entity):
  def __init__(self,x,y,graphic,max_hp,att,dif):
    Entity.__init__(self,x,y,graphic)
    self.max_hp=max_hp
    self.cur_hp=max_hp
    self.att=att
    self.dif=dif
  def attackmonster(self,Monster):
    pass
  def attackhero(self,Monster):
    pass
  def movement(self):
    pass
  
   
e = Mobile(5, 5, "X", 50,25,4)
m=Mobile(6,6,"M",20,10,5)
for y in range(10):
  for x in range(10):
    if e.x == x and e.y == y:
      print("[{}]".format(e.graphic), end="")
    elif m.x == x and m.y == y:
      print("[{}]".format(m.graphic), end="")
    else:
      print("[ ]", end="")

  print()