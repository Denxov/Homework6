import math


class Figure():
    sides_count=0
    __sides=[]
    __color=[0,0,0]
    filled=False
    def __init__(self,color,*args):
        self.__color=list(color)
        if self.is_valid_sides(*args):
            self.__sides=list(args)
        else: self.__sides=[1 for x in range(0,self.sides_count)]

    def get_color(self):
        return self.__color
    def __is_valid_color(self,r,g,b):
        return 0<=r<=255 and 0<=g<=255 and 0<=b<=255
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color=[r,g,b]
    def is_valid_sides(self,*args):
        ll=len(args)
        if ll!=self.sides_count:
            return False
        else:
            for i in range(0,ll-1): #len(args)):
                if type(args[i])!=int or  args[i]<=0:
                    return False
            return True

    def get_sides(self):
        return self.__sides
    def set_sides(self,*sides):
        if self.is_valid_sides(sides):
            self.__sides=list(sides)

    def __len__(self):
        len=0
        for i in self.__sides:
            len+=i
        return len

class Circle(Figure):
    sides_count=1
    def __init__(self,color,*args):
        self.radius=args[0]/math.pi/2
        super().__init__(color,args)
    def get_square(self):
        return math.pi*self.radius**2

class Triangle(Figure):
    sides_count=3
    def get_square(self):
        p=len(self)*0.5
        pp=p
        for x in self._Figure__sides:
            pp=pp*(p-x)
        return math.sqrt(pp)

class Cube(Figure):
    sides_count=12
    __sides=[]
    def __init__(self,color,*args):
        self.__sides=[args[0] for i in range(0,self.sides_count)]
        super().__init__(color,*self.__sides)

    def get_volume(self):
        volume=self.__sides[0]*self.__sides[1]*self.__sides[2]
        return volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1=Triangle((200,200,200),3,3,3)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(triangle1.get_square())
print(len(triangle1))

print(len(cube1))
print(circle1.radius)
print(circle1.get_square())
