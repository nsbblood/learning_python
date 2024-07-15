import time

class Dog:
    
    def __init__(self, name):
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark! Bark! Bark!')

    def looking(self,direction):
        print(self.name + 'Looking at me' + direction)

    def eating(self,food):
        print(self.name +' is eating '+ food)

    def running(self,move):
        print(self.name +' running to ' +move)

my_dog=Dog('Karabas ')
time.sleep(1)
my_dog.speak()
time.sleep(1)
my_dog.looking(' up')
time.sleep(1)
my_dog.eating('menemen')
time.sleep(1)
my_dog.running('left corner')


def multiplyByThree(val):
    return 3 * val

print(multiplyByThree(444))

(print(print('Hello, World!')))

#Karabas will love you :) 
#If you did not understand the codes just copy and ask gemini
#Need more practice 