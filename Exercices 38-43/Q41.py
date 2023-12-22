# No different way of code is written as the requirment is specificly mentioned in problem description 

li = [1,2,3,4,5,6,7,8,9,10]

squaredNumbers = map(lambda x: x**2, li) #returns map type object data 
print(list (squaredNumbers))  #converting the object into list 



#Solution number two 
def sqrs(item):
    return item ** 2


lst = [i for i in range(1,11)]
print(list(map(sqrs, lst)))
