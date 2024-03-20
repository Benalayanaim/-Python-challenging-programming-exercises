def EvenGenerator(n):
    i = 0
    while i<=n:
        if i%2==0:
            yield i 

        i+=1

n =int(input("Enter the Value: "))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))    


#Expalin for the program :
#Generator Function (EvenGenerator):

#The function EvenGenerator(n) is a generator function. It defines a loop that iterates from 0 to n.
#Inside the loop, it checks if i is an even number (i % 2 == 0).
#If i is even, it uses yield i. The yield statement pauses the function and produces a value (i). The state of the function is saved, allowing it to be resumed from this point later.
#After yielding a value, the function continues its execution from where it was paused.

#Generator Usage (for i in EvenGenerator(n):):

#The generator function is used in a for loop to iterate over the values it produces.
#The loop appends each even number to the values list.

#Printing the Result (print(",".join(values))):

#Finally, the program prints the even numbers in a comma-separated form.

#This use of yield in a generator is a memory-efficient way to generate values on the fly.
# It avoids creating an entire list of even numbers upfront, saving memory, especially when dealing with large ranges.
# The generator function produces values as needed, one at a time, during the iteration.


#Solution Number two 

n = int(input("Enter the value: "))
for i in range(0, n+1, 2):
    if i < n - 1:
        print(i, end = ',')

    else:
        print(i)      





#The Expalanation for this code :

#User Input (n):

#The program takes user input for the value of n.
        
1/#For Loop (for i in range(0, n+1, 2):):
#The loop iterates over even numbers in the range from 0 to n (inclusive), 
        #incrementing by 2 at each step. This is achieved using the range function with a step size of 2.


#2/Printing Even Numbers (print(i, end=',')):
#Inside the loop, the code prints each even number (i).
#The end=',' parameter in the print function ensures that 
        #the numbers are printed with a comma at the end instead of a newline character.


#3/Handling the Last Number (if i < n - 1: ... else: ...):
#The if condition checks if the current even number (i) is less than n - 1.
#If true, it means that the current even number is not the last one in the range. 
        #In this case, a comma is printed at the end to separate it from the next number.
#If false, it means that the current even number is the last one in the range,
        # and a newline is printed instead of a comma to end the line.        
