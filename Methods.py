#Methods
#Methods are like functions inside classes

#New class
class dog2(object):
    sp = 'Mammal'
    def __init__(self, race):
        self.race = race
        print(len(self.sp))
    def bark(self):
        print('Au Au')

James = dog2("Lab")
print(James.race)
print(James.sp)

James.bark()

#Another class with new methods
class circle1(object):
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def area1(self):
        return self.radius ** 2 * self.pi
    
    def defRadius1(self, radius):
        self.radius = radius

    def takeRadius1(self):
        return self.radius

#Initialize function
c = circle1()
#defines radius != 1
c.defRadius1(3)
#Print radius
print(c.radius)
#Print area
print(c.area1())
#Take radius value
radius_ex = c.takeRadius1()
print(radius_ex)