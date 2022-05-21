#Makes possible inherit old class

#creat new class
class Animal(object):
    def __init__(self):
        print('Animal created')
    
    def WhoAmI(self):
        print("I'm an animal")

    def eat(self):
        print('Eating...')

#Call methods test
#animal1 = Animal()
#animal1.WhoAmI()
#animal1.eat()

#create class to inherit 
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created.')
    
    def WhoAmI(self):
        print("I'am a dog")
    
    def bark(self):
        print('Au Au')

#Calls methods from Dog and Animal class
sam = Dog()
sam.WhoAmI()
sam.bark()
sam.eat()


