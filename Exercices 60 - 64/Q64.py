def generate(n):
    for i in range(n+1):
        if i % 35 == 0: #5*7 = 35 , if a number is divisible by a & b then it is divisible by a*b 
            yield i

n = int(input("Enter the value: "))
resp = [str(i) for i in generate(n)]
print(",".join(resp))



#Solution number two :

def print_divisible_by_5_and_7(n):
    values = [str(i) for i in range(0, n+1) if i % 5 == 0 and i % 7 == 0]
    print(",".join(values))

n = int(input("Enter the value of n: "))
print_divisible_by_5_and_7(n)




#Solution number 3:

def divisible_by_5_and_7(n):
    for i in range(0, n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter the value of n: "))
values = list(divisible_by_5_and_7(n))
print(",".join(map(str, values)))
