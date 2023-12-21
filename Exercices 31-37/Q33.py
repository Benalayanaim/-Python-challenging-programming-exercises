def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printList()   



#////////////////////////////////////////////////////////////////////////////

def generate_and_print_squares():
    # Generate a list of squares of numbers from 1 to 20
    squares_list = [num ** 2 for num in range(1, 21)]

    # Print the generated list
    print(squares_list)

# Call the function to generate and print the list of squares
generate_and_print_squares()


#This code defines a function generate_and_print_squares that generates a list 
# containing the squares of numbers from 1 to 20 (inclusive) and then prints the entire list.