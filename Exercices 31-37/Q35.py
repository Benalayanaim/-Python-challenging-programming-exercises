def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(19,14,-1):
        print(lst[i])

printList()



#/////////////////////////////////////////////////////////////
#Another solution 

def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[-5:])
squares(20)


#/////////////////////////////////////////////////////////////
#Another solution 
def print_first_five_squares():
    # Generate a list of squares of numbers from 1 to 20
    squares_list = [num ** 2 for num in range(1, 21)]

    # Print the first 5 elements in the list
    print(squares_list[-5:])

# Call the function to print the first 5 squares
print_first_five_squares()


