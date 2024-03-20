def f(n):
    if n < 2 :
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) +f(n-2)
    return fibo[n]

n = int(input("Enter the value: "))
fibo = [0]*(n+1) #initialze a list of size (n+1)
f(n)             #call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo] #converting integer data to string type
ans = ",".join(fibo) #joining all string element of fibo with ',' character
print(ans)



#Explanation id input 8 :


#Certainly! Let me explain how the program works step by step for the input 8:

#Initialization:

#The program initializes the Fibonacci sequence as [0, 1].
#Iteration:

#The program enters a loop starting from the 3rd element (i = 2) up to the specified n (in this case, 8).
#At each iteration, the program calculates the next Fibonacci number by adding the last two numbers in the sequence (fib_sequence[i - 1] + fib_sequence[i - 2]) and appends it to the sequence.
#Building the Sequence:

#Iteration 1 (i = 2): fib_sequence[2] = fib_sequence[1] + fib_sequence[0] = 1 + 0 = 1
#Iteration 2 (i = 3): fib_sequence[3] = fib_sequence[2] + fib_sequence[1] = 1 + 1 = 2
#Iteration 3 (i = 4): fib_sequence[4] = fib_sequence[3] + fib_sequence[2] = 2 + 1 = 3
#Iteration 4 (i = 5): fib_sequence[5] = fib_sequence[4] + fib_sequence[3] = 3 + 2 = 5
#Iteration 5 (i = 6): fib_sequence[6] = fib_sequence[5] + fib_sequence[4] = 5 + 3 = 8
#Iteration 6 (i = 7): fib_sequence[7] = fib_sequence[6] + fib_sequence[5] = 8 + 5 = 13
#Iteration 7 (i = 8): fib_sequence[8] = fib_sequence[7] + fib_sequence[6] = 13 + 8 = 21
#Result:

#The final Fibonacci sequence up to the 8th element is [0, 1, 1, 2, 3, 5, 8, 13, 21].
#The program then prints this sequence as output. Each number in the sequence is the sum of the two preceding numbers,
# following the Fibonacci sequence formula f(n) = f(n-1) + f(n-2).









#Solution number two:
def fibo(n):
    if n < 2 :
        return n 
    return fibo(n-1) + fibo(n-2)
def print_fiblist(n):
    fib_list = [(str(fibo(i))) for i in range(0, n+1)]
    return print(",".join(fib_list))
n = int(input("Enter the value: "))
print_fiblist(n)



#Expalin this code 

#1/Recursive Fibonacci Function (fibo):

#The function fibo(n) calculates the nth Fibonacci number.
#If n is less than 2, it returns n (base case).
#Otherwise, it recursively calculates fibo(n-1) + fibo(n-2).


#2/Print Fibonacci List Function (print_fiblist):

#The function print_fiblist(n) generates a list of Fibonacci numbers up to the nth element.
#It uses a list comprehension to create a list of strings,
# where each element is the result of calling fibo(i) for i ranging from 0 to n.
#Finally, it prints the list as a comma-separated string.

#3/User Input and Output:

#The program takes user input for the value of n.
#It then calls print_fiblist(n) to generate and print the Fibonacci sequence up to the nth element.