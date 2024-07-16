class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')
    
    def getLegs(self):
        return self._legs


class Chihuahua(Dog): #Class inherits from Dog
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')
        
    def wagTail(self):
        print('Vigorous wagging!')


my_chihuahua = Chihuahua("Coco")
my_chihuahua.speak()

