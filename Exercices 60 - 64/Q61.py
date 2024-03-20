def f(n):
    if n < 2 :
        return n
    return f(n-1) + f(n-2)
n = int(input("Enater the value: "))
print(f(n))



#Solution number Two 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input from the console
n = int(input("Enter the value of n: "))

# Calculate and display the result
result = fibonacci(n)
print(f"f({n}) = {result}")


#Explanation when i input 8

#Certainly! Let's break down the calculation for f(8) step by step using the Fibonacci sequence formula:

#Base Cases:

#f(0) = 0
#f(1) = 1
#Recursive Calculation:

#f(8) = f(7) + f(6)
#f(7) = f(6) + f(5)
#f(6) = f(5) + f(4)
#f(5) = f(4) + f(3)
#f(4) = f(3) + f(2)
#f(3) = f(2) + f(1)
#f(2) = f(1) + f(0)
#Substitute Base Cases:

#Now, we substitute the base cases into the recursive calculations:
#f(0) = 0
#f(1) = 1
#Backward Substitution:

#Substitute the values upward in the recursion tree:
#f(2) = f(1) + f(0) = 1 + 0 = 1
#f(3) = f(2) + f(1) = 1 + 1 = 2
#f(4) = f(3) + f(2) = 2 + 1 = 3
#f(5) = f(4) + f(3) = 3 + 2 = 5
#f(6) = f(5) + f(4) = 5 + 3 = 8
#f(7) = f(6) + f(5) = 8 + 5 = 13
#f(8) = f(7) + f(6) = 13 + 8 = 21
#So, the final result is f(8) = 21. The Fibonacci sequence builds up by adding the two previous numbers to get the next number in the sequence. 
#The recursive nature of the function reflects this pattern, 
#and each step involves breaking down the problem into simpler subproblems until reaching the base cases.
