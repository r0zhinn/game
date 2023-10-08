FALL_SPD             = 10
dtime                = None
class GameObject:
    def __init__(self,x=0,y=0,spdx=0,spdy=0,gravity=True) -> None:
        self.x       = x
        self.y       = y
        self.spdx    = spdx
        self.spdy    = spdy
        self.gravity = gravity
        objects.append(self)
    def fall(self):
        self.spdy   += FALL_SPD*dtime

    def move(self):
        self.x      += self.spdx
        self.y      += self.spdy
    def update(self):
        if self.gravity:
            self.fall()
        self.move()
        self.draw()
class Cube(GameObject):
    def draw(self):
        pass
    def set_size(self,size):
        pass




objects =[]