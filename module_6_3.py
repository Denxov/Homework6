class Animal():
    live=True
    sound=None
    _DEGREE_OF_DANGER = 0
    def __init__(self,name:str,speed:int):
        self.name=name
        self.speed=speed
        self.coords=[0,0,0]
    def move(self,dx,dy,dz):
        if self.coords[2]+dz*speed<0
            print("It's too deep, i can't dive :(")
        self.coords=[dx,dy,dz]