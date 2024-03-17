n = int(input("write the number: "))
sum = 0
for i in range(1, n+1):
    sum+= i/(i+1)

print(round(sum, 2))  #round to 2 decimal point     