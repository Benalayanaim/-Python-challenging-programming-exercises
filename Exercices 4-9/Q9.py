lst = []

while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print (line)    


 #Solution 2

def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s
        #In the provided code, the yield statement is used within the user_input() function to create a generator.
        #  Let me explain how it works:

#user_input() is a generator function. When you call this function, it doesn't execute immediately.
#  Instead, it returns a generator object.

#The while True: loop inside user_input() is an infinite loop that keeps reading input lines.

#s = input() reads a line of input from the user and assigns it to the variable s.

#if not s: checks if the line is empty (contains no characters). If the line is empty, the return statement is executed,
#  which exits the generator and effectively stops the loop.

#If the line is not empty, the yield s statement is executed. This yield statement yields (returns) the current value of s back to the caller of the generator,
# and the generator's state is temporarily paused.

#When the generator is paused, the control returns to the for loop in the main part of the program, which then processes the yielded value.

#The for line in map(str.upper, user_input()): loop iterates through each line of input, capitalizes the characters using str.upper,
#  and prints the capitalized line. When the loop needs the next line, it returns to the user_input() generator function,
#  which resumes execution from where it was paused by yield, reading the next line of input.

#This mechanism allows you to read and process lines of input one at a time without loading the entire input into memory at once, making it memory-efficient for processing large amounts of data.

for line in map(str.upper, user_input()):
    print(line)


#The main part of the program iterates through each line of input using a for loop: for line in map(str.upper, user_input()):. 
# It uses the map() function to apply str.upper (convert to uppercase) to each line read from the user_input() generator.

#Finally, it prints each line with all characters capitalized.

#When you run this program and provide input, it will capitalize all the characters in each input line and print the capitalized lines.








