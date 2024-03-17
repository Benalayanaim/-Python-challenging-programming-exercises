import re

email = input("put your text: ")
pattern = "\d+"
ans = re.findall(pattern,email)
print(ans)


#Explain ==> pattern = "\d+" :

#In Python, the pattern "\d+" is a regular expression that is used to match sequences of one or more digits.
# Here's a breakdown of what each part of the pattern means:

#\d: This is a special character class in regular expressions that represents any digit (0-9).

# +: This is a quantifier that means "one or more occurrences of the preceding element.
#" In this case, it applies to the \d character class, indicating one or more digits.





#Another solution

email = input("write your text: ").split()
ans = []
for word in email:
    if word.isdigit(): #can also use isnumeric() / isdecimal() function instead
        ans.append(word)
print(ans)        



#Another Solution
email = input().split()
ans = [word for word in email if word.isdigit()] #using list comprehension method 
print(ans)
