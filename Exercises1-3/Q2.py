# Using While Loop 
n = input("") #input() function takes input as string type

n = int(n) # convert it to integer type
fact = 1
i = 1
while i <= n :
    fact = fact * i
    i += 1 
print(fact)      


#Using For Loop
n = int(input())

fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)    


#Using Lambda Function 
n = int(input())
def shortfact(x):
    return 1 if x <= 1 else x*shortfact(x-1) 
print(shortfact(n))



#Using reduce
from functools import reduce 

def fun(acc, item):
    return acc*item

num = int(input())
print(reduce(fun,range(1, num+1), 1))

#Reduce how work 

#The reduce function is used to perform a specific operation on a sequence of values.
#  In this case, it will be used to multiply all the numbers from 1 to num together to calculate the factorial.

#A custom function fun is defined, which will be used as the operation to apply to the values in the sequence.
#  This function takes two arguments, acc (short for "accumulator") and item. It returns the product of acc and item, which effectively accumulates the product of all the items in the sequence.

#The reduce function is called as follows:

print(reduce(fun, range(1, num + 1), 1))
#reduce takes three arguments:
#The first argument is the function (fun) to apply cumulatively to the items in the sequence.
#The second argument is the sequence itself, which is generated using range(1, num + 1). This creates a sequence of numbers from 1 to num.
#The third argument is the initial value for the accumulator, which is set to 1. This is the starting point for the multiplication.
#The reduce function then performs the following operations:

#Initially, acc is set to 1 (the initial value), and item is set to the first element of the sequence (1).
#It applies the fun function to these values, so acc becomes 1 * 1 = 1.
#Then, acc is set to 1 (the result of the previous step) and item is set to the next element in the sequence (2).
#This process continues, accumulating the product of the numbers from 1 to num through the fun function.
#The result is printed using print, which will be the factorial of the input num.
