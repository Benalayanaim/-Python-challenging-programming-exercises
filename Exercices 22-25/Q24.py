print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)


#Certainly! Your program is using the .__doc__ attribute to access the docstring of various functions.
#  The docstring is a string that provides documentation and information about a function, class, or module in Python.
#  Let's break down your code:

print(str.__doc__)
#This line prints the docstring for the str class. 
# The str class is the built-in class for strings in Python, and .__doc__ retrieves its documentation.

print(sorted.__doc__)
#This line prints the docstring for the sorted function. 
# The sorted function is used to sort iterables, and its docstring provides information about how to use it.


def pow(n, p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''
    return n**p
#Here, you define a custom function pow that calculates n to the power p.
#  The function has a docstring enclosed in triple quotes (''' ... '''), 
# providing information about the parameters and the return value of the function.

print(pow(3, 4))
#This line calls your custom pow function with arguments 3 and 4, printing the result of 3^4.

print(pow.__doc__)
#This line prints the docstring of your custom pow function.
#  It uses .__doc__ to access the docstring associated with the function.

#In summary, your program demonstrates the use of .__doc__ to access and print the docstrings of the built-in str class,
#  the sorted function, and your custom pow function.
#  Docstrings are useful for providing information about
#  the purpose, usage, and parameters of functions or classes, making it easier for others (and yourself) to understand and use the code.




