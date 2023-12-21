def printList():
    lst = [i ** 2 for i in range (1,21)]

    for i in range(5):
        print(lst[i])

printList()


#////////////////////////////////////////////////////////

#Another Solution 
def squares(n):
    squares_list = [i ** 2 for i in range(1,n+1)]
    print(squares_list[0:5])

squares(20)

#////////////////////////////////////////////////////////

#Another Solution 

func = lambda : print([i ** 2 for i in range(1,21)][:5])

func()


#////////////////////////////////////////////////////////

#Another Solution 

def print_first_five_squares():
    # Generate a list of squares of numbers from 1 to 20
    squares_list = [num ** 2 for num in range(1, 21)]

    # Print the first 5 elements in the list
    print(squares_list[:5])

# Call the function to print the first 5 squares
print_first_five_squares()




#This code defines a function print_first_five_squares that generates a list containing
#  the squares of numbers from 1 to 20 (inclusive). The function then prints the first 5 elements of the generated list 
# using slicing ([:5]).