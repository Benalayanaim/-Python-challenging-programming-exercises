word = input()
upper,lower = 0,0

for i in word:
    if 'a'<= i and i<='z':
        lower +=1

    if 'A'<= i and i<= 'Z':
        upper +=1

print("UPPER CASE {0}\n LOWER CASE {1}".format(upper,lower))     


#solution number 2
word = input()

upper = sum(1 for i in word if i.isupper())  #sum function cumulatatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\n LOWER CASE {1}".format(upper,lower))
