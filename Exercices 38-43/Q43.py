def Even_Element(x):
    return x % 2 ==0

evenNumbers = filter(Even_Element, range(1,21))
print(list(evenNumbers))



#Soltion Numbers Two 
# Using filter() to create a list of even numbers between 1 and 20
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))

# Print the result
print(even_numbers)


    


    