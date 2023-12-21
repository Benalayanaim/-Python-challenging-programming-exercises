def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()


#////////////////////////////////////////////////////////////////////////////
#Another solution 

def print_keys_of_squared_dictionary():
    # Create a dictionary with keys as numbers from 1 to 20 and values as their squares
    squared_dict = {num: num ** 2 for num in range(1, 21)}

    # Print only the keys
    for key in squared_dict.keys():
        print(key)

# Call the function to print the keys of the squared dictionary
print_keys_of_squared_dictionary()


#In this code, the function print_keys_of_squared_dictionary generates a dictionary 
# where the keys are numbers from 1 to 20 (inclusive) and the values are the squares of the corresponding keys. 
# The function then prints only the keys from the generated dictionary.