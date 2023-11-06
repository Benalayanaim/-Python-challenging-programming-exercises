#Using for loop
n = int(input())
ans = {}
for i in range (1, n+1):
    ans[i] = i * i
print(ans)

#Using dictionary comprehension
n = int(input())
ans = {i : i*i for i in range(1 , n+1)}
print(ans)

#Using try and execpt
try:
    num = int(input("enter a number: "))
except ValueError as err:
    print(err)

dictio = dict()
for item in range(num+1):
    if item == 0:
        continue
    else:
        dictio[item] = item * item
print(dictio)        

#Using dict and enumerate
num = int(input("Number: "))
print(dict(enumerate([i*i for i in range(1, num+1)], 1)))

