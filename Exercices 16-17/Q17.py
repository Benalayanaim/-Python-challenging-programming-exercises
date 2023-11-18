total = 0
while True:
    s = input().split()
    if not s:         #break if the strings is emptyy
        break

    cm,num = map(str,s)  #two inputs are distributed in cm and num in strinngs 
    if cm == 'D':
        total +=int(num)

    if cm =='W':
        total -=int(num)

print(total)  

#input for like this for Exmaple and it sum the D and it sum(D)-sum(W)

#D 100
#D 200
#W 300
#D 300 

# Another Solution
transactions = []

while True:
    text = input(">")
    if text :
        text = text.strip('D ')
        text = text.replace('W ','-')
        transactions.append(text)
    else:
        break
transactions = (int(i) for i in transactions)
balance = sum(transactions)
print(f'Balnce is {balance}')

#Expalination about Strip 
#In the given program, the strip() method is used to remove leading and trailing characters from the input string text. 
# Specifically, it is used to remove the characters 'D' and space from the beginning of the string. Here's the relevant line:

text = text.strip('D ')
#Let's break it down:

#text.strip('D '): This method will remove any leading or trailing occurrences of the characters 'D' or space (' ') from the string text.
#So, for example, if the input is "D 100", after applying strip('D '),
#  the value of text becomes "100" (with leading and trailing spaces removed).

#The replace() method is then used to replace occurrences of 'W ' with '-' in the string:


text = text.replace('W ', '-')
#Here, it replaces 'W ' with '-' in the string. This is done to handle the case where withdrawals are represented by 'W ' in the input.

#Overall, these operations are preparing the input for conversion to integers and subsequent addition to the transactions list.
#  If you have further questions or need more clarification, feel free to ask!




