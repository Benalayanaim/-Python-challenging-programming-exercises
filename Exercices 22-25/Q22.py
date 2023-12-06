ss = input().split()
word = sorted(set(ss))  #split words  are sorted as a set

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))

#The line print("{0}:{1}".format(i, ss.count(i))) is using a string formatting technique in Python. Let me break it down for you:

#The string "{}:{}" is a format string where {0} and {1} are placeholders for values that will be inserted into the string.

#.format(i, ss.count(i)) is a method applied to the string.
#  The values of i and ss.count(i) will be substituted into the placeholders {0} and {1}, 
# respectively.

#So, if i is a word and ss.count(i) is the count of that word in the original list ss,
#  the line is essentially creating a string where {0} is replaced by the word i and {1} is replaced by its count.





#Another solution 
ss = input().split()
dict = {}
for i in ss :
    i = dict.setdefault(i,ss.count(i))   #setdefault() function takes key and value set it as dictioanary.

dict = sorted(dict.items())   #items() function returns both key and value of dictionary as a list 
                             # and then sorted. the sort by default occurs in order of 1st -> 2nd key
for i in dict :  
    print("%s:%d"%(i[0],i[1]))


    #Certainly, let's break down the last part of the code:

for i in dict:
    print("%s:%d" % (i[0], i[1]))
#Here, dict is a dictionary that has been populated with words as keys and their corresponding counts as values. 
# The for loop is iterating over the items of the dictionary, where each item is a key-value pair.

#i takes the value of each item in the loop, and since each item is a tuple (key, value), i[0] corresponds to the key (word), 
# and i[1] corresponds to the value (count).

#"%s:%d" % (i[0], i[1]) is a string formatting technique similar to the one used in the previous solution. 
# Here, %s is a placeholder for a string (i[0]), and %d is a placeholder for an integer (i[1]).

#So, for each iteration of the loop,
#  it prints a string where i[0] (the word) is substituted for %s and i[1] (the count) is substituted for %d.
#  The result is a string in the format "word:count".

#For example, if the dictionary contains the item ('apple', 3), then this part of the code will print:


apple:3
#This loop effectively prints each word along with its count in a formatted way for all items in the dictionary.