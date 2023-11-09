def check(x):    #converts binary to integer & returns zero if divisible by 5
    total,pw = 0,1 #The total variable is initialized to 0, and pw is initialized to 1.

#reversed(x) is called, but the result is not assigned to any variable, 
# so it doesn't have any effect on the code. To reverse a string, you should assign the result back to the variable.

#The code then iterates through each character in the binary number x. 
# It multiplies each digit (0 or 1) by the appropriate power of 2 (2^0, 2^1, 2^2, ...) and accumulates the result in the total variable.

#Finally, it calculates total % 5 and returns the result, which will be 0 if the binary number is divisible by 5.
    reversed(x)

    for i in x :
        total+= pw * (ord(i) - 48) #ord() function returns ASCII value
        pw*=2
    return total % 5

data =  input().split(",") #inputs taken here and splited in ',' position 
lst =[]

for i in data :
    if check(i) == 0:   #if zero found it means divisible by zero and added to the list
        lst.append(i)

print(",".join(lst))




#Explain for this code 
#for i in x :
 #   total+= pw * (ord(i) - 48) #ord() function returns ASCII value
  #  pw*=2
#return total % 5

#x is a string representing a binary number, and the for loop iterates through each character in the string.

#ord(i) is used to obtain the ASCII value of the character i. In this context,
#  i is a character representing a digit in the binary number, either '0' or '1'. The ASCII value of '0' is 48, 
# and the ASCII value of '1' is 49. Subtracting 48 from ord(i) effectively converts '0' to 0 and '1' to 1,
#  giving you the integer value of the digit.

#pw is used to calculate the position value of the digit within the binary number. 
# It starts at 1 and is doubled with each iteration. For example, in the binary number 1101, 
# the rightmost '1' has a position value of 1, the next '0' has a position value of 2, the next '1' has a position value of 4,
#  and the leftmost '1' has a position value of 8.

#total is used to accumulate the sum of the decimal values of the binary digits,
#  taking into account their positions. For each digit in x, 
# total is updated by adding the product of the decimal value of the digit and its position value to the current value of total.

#Finally, total % 5 calculates the remainder when total is divided by 5. 
# If the remainder is 0, it means the original binary number is divisible by 5, and the function returns 0.

#To summarize, this code segment converts a binary number into its decimal equivalent by iterating through the binary digits, 
# calculates the sum of these decimal values, and then checks if the resulting integer is divisible by 5. If it is divisible,
#  the function returns 0; otherwise, it returns a non-zero value.





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Solution number 2
data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))  #lambda is an operator that helps to wirte function of one line 
print(",".join(data))


#The filter function is used to create a new list that contains only the elements from the data list that satisfy the given condition.
#  In this case, a lambda function is used as the condition.
#  The lambda function takes an element i from the data list and converts it from binary to an integer using int(i, 2). 
# Then, it checks if the resulting integer is divisible by 5 (int(i, 2) % 5 == 0).

#The filter function creates an iterator of elements that meet the condition, 
# so list(...) is used to convert this iterator back into a list. 
# The resulting list contains only the binary numbers that are divisible by 5.

