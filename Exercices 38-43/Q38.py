tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range (0,5):
    print(tpl[i],end = ' ')
print()
for i in range(5,10):
    print(tpl[i],end = ' ')


#solution Number 2

tpl = (1,2,3,4,5,6,7,8,9,10)

lst1,lst2 = [],[]

for i in range(0,5):
    lst1.append(tpl[i])

for i in range(6,10):
    lst2.append(tpl[i])

print(lst1)
print(lst2)

#Solution number 3
tup = [i for i in range(1,11)]
print(f'{tuple(tup[:5])} \n {tuple(tup[5:])}')