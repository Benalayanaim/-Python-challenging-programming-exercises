class American():
    pass

class NewYorker(American):
    pass

# Creating instances of the classes
american = American()
newyorker = NewYorker()

# Printing the instances
print(american)  # Output: <__main__.American object at 0x...>
print(newyorker)  # Output: <__main__.NewYorker object at 0x...>


#Explain

#Your solution is correct! You've defined a base class American and a subclass NewYorker that inherits from American. 
#In your code, you've created instances of both classes, american and newyorker, and then printed them.
#When you print instances of classes in Python, you'll see something like <__main__.ClassName object at 0x...>. 
#This indicates that you have created instances of the classes successfully.





#Another solution
class American:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}, an American."

class NewYorker(American):
    def __init__(self, name, borough):
        super().__init__(name)
        self.borough = borough

    def greet(self):
        return f"Hey, I'm {self.name}, a New Yorker from {self.borough}."

# Example usage:
american_person = American("John Doe")
newyorker_person = NewYorker("Jane Smith", "Manhattan")

print(american_person.greet())  # Output: Hello, I'm John Doe, an American.
print(newyorker_person.greet())  # Output: Hey, I'm Jane Smith, a New Yorker from Manhattan.
