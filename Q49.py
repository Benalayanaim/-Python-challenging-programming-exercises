class Shape():
    def __init__(self):
        pass

    def area(self): 
        return 0 #In this code, a class named Shape is defined. It has an __init__ method (constructor) 
    #that doesn't do anything specific (it just contains the pass statement), 
    #and an area method that returns 0. This means that by default, the area of any object created from the Shape class will be 0.
    
class Square(Shape):
    def __init__(self, length = 0):
         Shape.__init__(self)
         self.length = length

    def area(self):
        return self.length*self.length #Here, a subclass named Square is defined, which inherits from the Shape class. The Square class has its own __init__ method,
    # which takes an optional length parameter (defaulting to 0). Inside the __init__ method, 
    #it first calls the __init__ method of the base class (Shape.__init__(self)) to initialize any properties of the Shape class.
    # Then, it initializes its own length attribute.    

#The Square class also has its own area method, which calculates and returns the area of the square using the formula ==> length×length.
Asqr = Square(5)
print(Asqr.area())   #print 25 as given argument
print(Square().area())# prints 0 as default area  






#Solution Number two

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

# Example usage:
shape = Shape()
print(f"Area of Shape: {shape.area()}")  # Output: Area of Shape: 0

square = Square(4)
print(f"Area of Square: {square.area()}")  # Output: Area of Square: 16



###Explain :

#In this code, the Shape class has an area method that returns 0 by default. 
#The Square class inherits from Shape and has its own __init__ method to initialize the length. 
#The area method in the Square class calculates the area of the square using the formula :

#length×length.


#The example usage at the end demonstrates creating instances of both Shape and Square classes and calling their area methods.