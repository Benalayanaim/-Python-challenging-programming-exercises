x,y = map(int,input().split(','))
lst  = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)

    lst.append(tmp)

print(lst)        

#Your solution is correct and accomplishes the same task as the one I provided earlier.
#  It creates a 2-dimensional array and fills it with values calculated as i * j for each element in the array.

#Here's how your solution works:

#It takes input for X and Y as comma-separated values.
#It initializes an empty list lst to store the 2-dimensional array.
#It uses nested loops to iterate through the rows and columns of the array.
#For each row (i), it initializes an empty list tmp to store the values for that row.
#For each column (j), it calculates the value i * j and appends it to the tmp list.
#After filling the tmp list for each row, it appends the tmp list to the main list lst.
#Finally, it prints the resulting 2-dimensional array.
#Your solution is a valid and working approach to generate the desired 2-dimensional array. It's a good example of using loops to build the array element by element.

#Solution2
x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)]for i in range(x)]
print(lst)