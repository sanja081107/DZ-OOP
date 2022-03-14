globs = globals()

class Warrior:

    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def __str__(self):
        s1 = '---------------\n'
        s2 = f'Class: {self.__class__.__name__}\n'
        s3 = f'Health: {self.health}\n'
        s4 = f'Stamina: {self.stamina}\n'
        s5 = '---------------'
        return s1 + s2 + s3 + s4 + s5

    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def __add__(self, target):

        if isinstance(target, int):
            self.stamina -= 10
            if self.stamina < 0: self.stamina = 0
            self.health += target
            if self.health > 100: self.health = 100
            print('---------------')
            print(f'{self.__class__.__name__} лечит себя')
            print(f'Здоровье у {self.__class__.__name__} повышено до {self.health}')
            print(f'У {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
            print('---------------')

        if isinstance(target, Mage) or isinstance(target, Warrior):
            self.stamina -= 10
            if self.stamina < 0: self.stamina = 0
            target.health += 10
            if target.health > 100: target.health = 100
            print('---------------')
            print(f'{self.__class__.__name__} лечит {target.__class__.__name__}')
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}')
            print(f'У {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
            print('---------------')

        if isinstance(target, list):
            target.append(self)
            for i in globs:
                if id(globs[i]) == id(target):
                    print(f'{self.__class__.__name__} присоеденился к отряду {i}')
                    break

    def __sub__(self, target):

        if isinstance(target, int):
            self.health -= target
            if self.health < 0: self.health = 0
            print('---------------')
            print(f'{self.__class__.__name__} калечит себя на -{target}')
            print(f'Здоровье у {self.__class__.__name__} понижено до {self.health}')
            print('---------------')

        if isinstance(target, Mage) or isinstance(target, Warrior):
            self.health -= 10
            if self.health < 0: self.health = 0
            print('---------------')
            print(f'{self.__class__.__name__} был аттакован {target.__class__.__name__}(-ом)')
            print(f'Здоровье у {self.__class__.__name__} понижено до {self.health}')
            print('---------------')

        if isinstance(target, list):

            target.remove(self)
            for i in globs:
                if id(globs[i]) == id(target):
                    print('---------------')
                    print(f'{self.__class__.__name__} вышел с отряда {i}')
                    print('---------------')
                    break


class Mage(Warrior):

    def __init__(self, health=100, mana=100):
        super(Mage, self).__init__(health)
        self.mana = mana

    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}')
        print(f'Health: {self.health}')
        print(f'Mana: {self.stamina}')
        print('---------------')

    def __str__(self):
        s1 = '---------------'
        s2 = f'Class: {self.__class__.__name__}'
        s3 = f'Health: {self.health}'
        s4 = f'Mana: {self.mana}'
        s5 = '---------------'
        return s1 + s2 + s3 + s4 + s5

    def __add__(self, target):

        if isinstance(target, int):
            self.mana -= 10
            if self.mana < 0: self.mana = 0
            self.health += target
            if self.health > 100: self.health = 100
            print('---------------')
            print(f'{self.__class__.__name__} лечит себя')
            print(f'Здоровье у {self.__class__.__name__} повышено до {self.health}')
            print(f'У {self.__class__.__name__} осталось {self.mana} единиц запаса маны')
            print('---------------')

        if isinstance(target, Mage) or isinstance(target, Warrior):
            self.mana -= 10
            if self.mana < 0: self.mana = 0
            target.health += 10
            if target.health > 100: target.health = 100
            print('---------------')
            print(f'{self.__class__.__name__} лечит {target.__class__.__name__}')
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}')
            print(f'У {self.__class__.__name__} осталось {self.mana} единиц запаса маны')
            print('---------------')

        if isinstance(target, list):
            target.append(self)
            for i in globs:
                if id(globs[i]) == id(target):
                    print('---------------')
                    print(f'{self.__class__.__name__} присоеденился к отряду {i}')
                    print('---------------')
                    break

    def __sub__(self, target):

        super().__sub__(target)



squad = []
unit1 = Warrior(60, 20)
unit2 = Mage(50, 70)

unit2 - unit1
unit2 + squad
unit1 - 20
unit1 - unit2
unit1 + squad
unit1 - squad


