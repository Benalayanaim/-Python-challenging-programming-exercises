class American():
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()











#Another Solution 

class American:
    nationality = "American"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

    def introduce(self):
        return f"Hello, I'm {self.name}."

    def say_hello(self):
        return "Hello from an American!"

    @staticmethod
    def printNationality():
        return f"All Americans are {American.nationality}."

# Example usage:
person = American("John Doe")

print(person.introduce())  # Output: Hello, I'm John Doe.
print(person.say_hello())  # Output: Hello from an American!
print(American.printNationality())  # Output: All Americans are American.











#In this example:

#The American class has a static method printNationality decorated with @staticmethod. Static methods don't have access to instance-specific data and are defined with the @staticmethod decorator.
#The __init__ method is the constructor, creating an instance with a given name.
#The introduce method returns a string introducing the person.
#The say_hello method returns a generic greeting.