from random import random


class Animal():
    live=True
    sound=None
    _DEGREE_OF_DANGER = 0
    def __init__(self,speed:int):
        self.speed=speed
        self.coords=[0,0,0]
    def move(self,dx,dy,dz):
        if self.coords[2]+dz*self.speed<0:
            print("It's too deep, i can't dive :(")
        self.coords[0]+=dx*self.speed
        self.coords[1]+=dy*self.speed
        self.coords[2]+=dz*self.speed

    def get_cords(self):
        print(f'X={self.coords[0]} Y={self.coords[1]} Z={self.coords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER<5:
            print("Sorry, i'm peaceful :)")
        else: print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self,dz):
        self.coords[2]-=abs(dz)*self.speed*0.5

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal,AquaticAnimal,Bird):
    sound="Click-click-click"
    def lay_eggs(self):
        eggs_count=int(random()*4)+1
        print(f'Here are(is){eggs_count} eggs for u')

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

