def printDict():
    dict={i:i**2 for i in range(1,21)} #using comprehension method and 
    print(dict)

printDict()    


#////////////////////////////////////////////////

#Another solution :

def print_squared_dictionary():
    # Create an empty dictionary
    squared_dict = {}

    # Populate the dictionary with keys and their squares
    for num in range(1, 21):
        squared_dict[num] = num ** 2

    # Print the resulting dictionary
    for key, value in squared_dict.items():
        print(f"{key}: {value}")

# Call the function to print the squared dictionary
print_squared_dictionary()






#This code defines a function print_squared_dictionary that creates a dictionary
#  where the keys are numbers from 1 to 20 (inclusive) and the values are the squares of the corresponding keys. 
# The function then prints each key-value pair in the dictionary