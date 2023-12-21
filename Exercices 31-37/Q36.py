def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5,20):
        print(lst[i])

printList()

#/////////////////////////////////////////////////////////////
#Another solution 
def generate_and_print_squares_excluding_first_five():
    # Generate a list of squares of numbers from 1 to 20
    squares_list = [num ** 2 for num in range(1, 21)]

    # Print all values except the first 5 elements in the list
    print(squares_list[5:])

# Call the function to generate and print squares excluding the first five
generate_and_print_squares_excluding_first_five()



#This code defines a function generate_and_print_squares_excluding_first_five that generates a list 
# containing the squares of numbers from 1 to 20 (inclusive) and then prints all values in the list
#  except the first 5 elements using slicing ([5:]).