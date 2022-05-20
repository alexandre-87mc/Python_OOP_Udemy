#Class

#Class can be called data type
l = [1,2,3] #List data type

#We can creat new data types
class Sample(object):
    pass
x = Sample()
print(type(x))

#New class exemple
class Dog(object):
    def __init__(self, race):
        self.race = race

sam = Dog(race='Lab')
print(sam.race)

#frank = Dog() #Don't work
#New dog
frank = Dog('Huskie')
print(frank.race)

#We can define countless ways and class
class dog2(object):
    sp = 'Mammal'
    def __init__(self, race):
        self.race = race
        self.numcaract = len(self.sp)

james = dog2('Golden')
print(james.race)
print(james.sp)
print(james.numcaract)
