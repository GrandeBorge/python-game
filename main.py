class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic
class Hero(Entity):
  def __init__(self,x,y,graphic,max_hp,att,dif):
    Entity.__init__(self,x,y,graphic)
    self.max_hp=max_hp
    self.cur_hp=max_hp
    self.att=att
    self.dif=dif
  def attack(self,Monster):
    if (self.x==Monster.x and self.y==Monster.y) or (self.x==Monster.x-1 and self.y==Monster.y) or (self.x==Monster.x+1 and self.y==Monster.y) or (self.x==Monster.x and self.y==Monster.y-1) or (self.x==Monster.x and self.y==Monster.y+1):
      Monster.cur_hp-=(Hero.att/100*Monster.dif)
  def movement(self):
    while True:
      movimento=input()
      if movimento=="w":
        self.y-=1
        if self.y<0: 
          self.y+=1
        else: 
          break
      elif movimento=="s":
        self.y+=1
        if self.y>9: 
          self.y-=1
        else: break
      elif movimento=="d":
        self.x+=1
        if self.x>9: 
          self.x-=1
        else: 
          break
      elif movimento=="a":
        self.x-=1
        if self.x<0: 
          self.x+=1
        else: 
          break
class Monster(Entity):
  def __init__(self,x,y,graphic,max_hp,att,dif):
    Entity.__init__(self,x,y,graphic)
    self.max_hp=max_hp
    self.cur_hp=max_hp
    self.att=att
    self.dif=dif
  def attack(self,Hero):
    if (self.x==Hero.x and self.y==Hero.y) or (self.x==Hero.x-1 and self.y==Hero.y) or (self.x==Hero.x+1 and self.y==Hero.y) or (self.x==Hero.x and self.y==Hero.y-1) or (self.x==Hero.x and self.y==Hero.y+1):
      Hero.cur_hp-=(self.att/100*Hero.dif)
  def movement(self, x,y):
    dx=Monster.x-x
    if dx<0: 
      dx2=dx*-1
    else:
      dx2=dx
    dy=Monster.y-y
    if dy<0: 
      dy2=dy*-1
    else:
      dy2=dy
    if random.randint(1,5)==(1 or 2):
      print("- Il mostro è confuso! -")
      move=random.randint(1,4)
      if move==1:
        Monster.x+=1
      elif move==2:
        Monster.x-=1
      elif move==3:
        Monster.y+=1
      elif move==4:
        Monster.y-=1
    else:
      if dx2>dy2:
        if dx<0:
          Monster.x+=1
        else:
          Monster.x-=1
      else:
        if dy<0:
          Monster.y+=1
        else:
          Monster.y-=1
e = Hero(5, 5, "X", 50,25,4)
m=Monster(6,6,"M",20,10,5)
for y in range(10):
  for x in range(10):
    if e.x == x and e.y == y:
      print("[{}]".format(e.graphic), end="")
    elif m.x == x and m.y == y:
      print("[{}]".format(m.graphic), end="")
    else:
      print("[ ]", end="")

  print()