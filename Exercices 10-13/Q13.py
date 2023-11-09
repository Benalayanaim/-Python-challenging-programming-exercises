
word = input()
letter,digit = 0,0


for i in word:
    if('a' <= i and i<='z') or ('A' <=i and i<='Z'):
        letter +=1

    if '0' <=i and i<='9':
        digit +=1

print("LETTERS {0}\nDIDGITS {1}".format(letter,digit))



#The last line of the program uses the .format() method to format and
#  print the values of letter and digit in a specific way within the string. Let me break it down for you:

#"LETTERS {0}\nDIDGITS {1}" is a string that contains two placeholders {0} and {1}.
#  These placeholders are used to indicate where values should be inserted into the string.

#.format(letter, digit) is a method that takes the values of letter 
# and digit and inserts them into the corresponding placeholders in the string. 
# The values are inserted in the order they appear in the .format() method.

#Here's what the line does:

#{0} gets replaced with the value of the letter variable.
#{1} gets replaced with the value of the digit variable.
#So, if letter contains, say, 5 and digit contains 3, the line will be printed as:


#Copy code
#LETTERS 5
#DIDGITS 3
#It formats the output to display the count of letters and digits in the word variable.
#  The values of letter and digit are substituted into the string where the placeholders are, and the resulting string is printed to the console.



#solution number 2
word =  input()
letter, digit = 0,0

for i in word :
    if i.isalpha():     #returns True if alphabet 
        letter += 1 

    elif i.isnumeric(): #returns true if numeric
        digit +=1

print(f"LETTERS {letter}\nDIDGITS {digit}") #two different types of formating method is shown in both solution



#solution number 3
import re

input_string = input('> ')
print()
counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}

print(counter)


#In the code you provided, the re module is used for regular expressions. Regular expressions are a powerful tool for pattern matching in strings. 
# Let's break down what the code is doing:

#import re: This line imports the Python re module, which provides functions and classes for working with regular expressions.

#input_string = input('> '): This line prompts the user to enter a sentence and stores the input as a string in the input_string variable.

#The re.findall() function is used twice in the code with different regular expressions to count the number of letters and digits in the input_string.

#re.findall("[a-zA-Z]", input_string) finds all the lowercase and uppercase letters in the input_string. 
# It uses the regular expression [a-zA-Z], which matches any single character that is a letter (a to z or A to Z).

#re.findall("[0-9]", input_string) finds all the digits in the input_string.
#  It uses the regular expression [0-9], which matches any single digit from 0 to 9.

#The results of these re.findall() calls are used to calculate the number of letters and digits in the input string.
#  The len() function is used to count the elements returned by re.findall(), which are the matching characters.

#The counts are stored in a dictionary named counter,
#  where "LETTERS" represents the count of letters and "NUMBERS" represents the count of digits.

#Finally, print(counter) is used to print the dictionary, displaying the count of letters and digits in the input string.

#The re module is not necessary for this specific task,
#  as you can achieve the same result using simpler methods. However, it is often used when dealing with more complex pattern matching and text manipulation tasks where regular expressions are required.




