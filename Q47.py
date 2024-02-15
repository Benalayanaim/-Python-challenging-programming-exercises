class Circle():
    def __init__(self, r) :
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle =Circle(5)
print(circle.area())       


#Your code looks correct! It defines a Circle class with an __init__ method to initialize the radius and an area method 
#to compute the area of the circle. Then, it creates an instance of the Circle class with a radius of 5 and prints the computed area.