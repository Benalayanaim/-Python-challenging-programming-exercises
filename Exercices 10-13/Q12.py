#To solve this problem, you need to find all the numbers between 1000 and 3000 (both inclusive) 
#where each digit in the number is an even number (0, 2, 4, 6, or 8).
# You can achieve this by iterating through the numbers in the given range and checking the digits of each number. 
#If all digits are even, add that number to a list. Finally,
# print the list of numbers in a comma-separated sequence. Here's a Python program to do this:

lst = []
for i in range(1000, 3001):
    flag = 1
    for j in str(i):           #every integer number i is converted into string 
        if ord(j) % 2 !=0 :    #ord returns ASCII value and j is every digit of i
            flag = 0           #flag becomes zero if any odd digit found   
    if flag == 1:
        lst.append(str(i))     #i is stored in list as string 

print(",".join(lst))

#solution number 2
def check(element):
    return all(ord(i)%2 == 0 for i in element)   #all returns True if all digits i is even in element 

lst = [str(i) for i in range (1000,3001)]        #creates list of all given numbers with string data type 
lst = list(filter(check,lst))                    #filter removes element from list if check condition  fails                             

print(",".join(lst))


#solution number 3
from functools import reduce
#using reduce to check if the number has only even digits or not 
def is_even_and(bool_to_compare,num_as_char):
    return int (num_as_char)%2==0 and bool_to_compare

print(*(i for i in range(1000,3001) if reduce (is_even_and,str(i),True)),sep=',')






