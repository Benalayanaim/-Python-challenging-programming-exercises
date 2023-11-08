from math import sqrt #import specific functions as importing all using *
                      # is bad practice

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)
123
D = [int(i) for i in input().split(',')] #split in comma and set up
D = [int(i) for i in D] #converts string to integer
D = [calc(i) for i in D] #returns floating value by clac lethod for every item in D
D = [round(i) for i in D] #All the floating values are rounded
D = [str(i) for i in D] #All the integers are converted to string to be able to apply join operation 

print(",".join(D))


#Example when the input 100
#I understand the confusion. It seems there is an issue with the code you provided, and the calculated result is not what you expect. The formula to calculate Q is as follows:

#Q = Square root of [(2 * C * D) / H]

#With C = 50, H = 30, and D = 100, the calculation should be as follows:

#Q = sqrt((2 * 50 * 100) / 30)
#Q = sqrt((10000) / 30)
#Q = sqrt(333.33...)

#The result should be the square root of approximately 333.33, which is approximately 18.25, not 18.
#  If you are getting the output of 18, there might be an issue with the code or the input values. The code itself seems correct,
#  so please double-check your input and the actual code execution to ensure everything is working as expected.
#So, in the code, the calculated value of Q is being rounded to the nearest integer. 
# That's why the output is 18 instead of the more precise value of approximately 18.25.
#  If you want the result to be a rounded integer, you can keep this line of code as it is.




#Solution 2
from math import sqrt

C,H = 50,30

def clac(D):
    return sqrt((2*C*D)/H)

D = input().split(',')                  #splits in comma position and set up in List
D = [str(round(clac(int(i)))) for i in D]#using comprehension method . It works in order of the previous code 
print(",".join(D)) 


#Solution 3
my_list = [int(x) for x in input('').split(',')]
C, H, x= 50 ,30, []

for D in my_list:
    Q = ((2*C*D)/H)**(1/2)
    x.append(round(Q))

print(','.join(map(str, x)))    

#The calculated value of Q is then rounded to the nearest integer using the round() function, and the rounded value is appended to the list x:

x.append(round(Q))
#Finally, you use ','.join(map(str, x)) to convert the list of rounded values to a comma-separated string for printing:

print(','.join(map(str, x))
#This code essentially performs the same calculation as the previous code, but it rounds the result to the nearest integer and prints the rounded values as a comma-separated string.





#print(','.join(map(str, x))
# why we use map

#In the line of code print(','.join(map(str, x)), the map() function is used to apply the str() function to each element in the list x. Here's what each part of the code does:

#map(str, x) - This part of the code takes each element in the list x and applies the str() function to it.
#  This converts each integer in the list x into a string.

#','.join(...) - This part of the code takes the result of the map() function and joins the elements together into a single string. In this case, it uses a comma ,
#  as the separator to create a comma-separated string.

#The purpose of using map(str, x) is to convert the elements in the list x from integers to strings because the join() function expects a sequence of strings to join together. 
# By using map(str, x),
#  you ensure that all the elements in the list are strings, making it possible to join them with commas.




