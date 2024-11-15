class Vehicle():
    __COLOR_VARIANTS=['black','white','blue','orange','oceanblue','heavenblue','red','milky','custom']

    def set_color(self,color):
        if color.lower() in self.__COLOR_VARIANTS:# проверка на наличие цвета в базе
            self._color=color
            return self
        else:
            print(f'Нельзя сменить цвет на {color}')
            return self

    def __init__(self,owner,model,color,engine_power):
        self.owner=owner
        self.__model=model
        self.__engine_power=engine_power
        self.set_color(color)

    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self._color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: ',self.owner)

class Sedan(Vehicle):
    __PASSANGERS_LIMIT=5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.__engine_power=10 # значение атрибута не изменится


# Проверяем что поменялось
vehicle1.print_info()

