import globalvariables as gv
class Fruit:
    def __init__(self,id,radindex,x,y):
        self.id = id
        self.radindex = radindex
        self.radius = gv.fruitRadius[radindex]
        self.x = int(x)
        self.y = int(y)

    def __lt__(self, other):
        return self.x > other.x
    
    def __eq__(self, other):
        return self.radindex == other
    
    def include(self,fruit):
        dx = (int(self.x) - int(fruit.x))
        dy = (int(self.y) - int(fruit.y))
        if abs(dx) > self.radius or abs(dy) > self.radius:
            return False
        return (dx*dx + dy*dy) <= (self.radius*self.radius)