def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

printTupple()



#/////////////////////////////////////////////////////////////
#Another solution 

def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))

print(square_of_numbers())


