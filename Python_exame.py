#1 - Fill the class methods so that they accept 
#coordinates as a pair of tuples and return 
#the inclination and distance from the line
class Line(object):
    def __init__(self, coor1, coor2):
        self.coors1 = coor1
        self.coors2 = coor2
        print(self.coors1)
        print(self.coors2)
        print('Object line distance_slope created')
    def distance(self):
        #Distance between point
        x1,y1 = self.coors1
        x2,y2 = self.coors2
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        print("Dont't forget the parentheses when you call a function inside a class.")
        return print(dist)
    def slope(self):
        x1,y1 = self.coors1
        x2,y2 = self.coors2
        self.slope = (x1-x2) / (y1-y2)
        return print(self.slope)

#Call class methods
Distance_slope_line = Line((3,2),(8,10))
Distance_slope_line.distance()
Distance_slope_line.slope()


#2 - Fill the class methods so that we can 
#calculate his surface area and his volume
class cylinder(object):
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        print('Cylinder created')
    def volume(self):
        h = self.height
        r = self.radius
        volume_cy = self.pi*r**2 * h
        return print('The volume of the cylinder with radius = %r and height = %r is %r' %(r,h,volume_cy))
    def surface_area(self):
        h = self.height
        r = self.radius
        surface_cy = 2*self.pi*r * h
        return print('The surface area of the cylinder with radius = %r and height = %r is %r' %(r,h,surface_cy))

#call class methods
cylinder_1 = cylinder(2,2)
cylinder_1.volume()
cylinder_1.surface_area()
