lst= input("Enter a series of numbers separated by a comma: ").split(',') #the input is begin taken as string and as it is string it has a built in
                        #method name split ',' inside split function does split where it finds any ','
                        #and save the input as list in lst variable

tpl = tuple(lst)
print(lst)
print(tpl) 


#Solution 2
print(tuple(input("Enter a series of numbers separated by a comma :").split(','))) 
