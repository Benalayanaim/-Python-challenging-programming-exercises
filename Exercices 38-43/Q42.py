def even(x):
    return x%2 ==0

def squer(x):
    return x*x
li = [1,2,3,4,5,6,7,8,9,10]

li = map(squer,filter(even,li)) #first filters number by even number and the apply map() on the resultant elemnets 

print(list(li))


#solution number two

def even(item):
    if item % 2 == 0:
        return item**2

lst = [i for i in range(1,11)]
print(list(filter(lambda j: j is not None, list(map(even, lst)))))    