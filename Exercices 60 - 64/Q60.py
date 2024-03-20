def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

n = int(input("wite the number: "))
print(f(n))

#Explanation for the input 

#Enter the value of n: 5
#f(5) = 500

#--So the ouput like this it calculate 
#f(5) = f(4) + 100
#     = (f(3) + 100) + 100
#     = ((f(2) + 100) + 100) + 100
#     = (((f(1) + 100) + 100) + 100) + 100
#     = ((((f(0) + 100) + 100) + 100) + 100) + 100
#     = ((((0 + 100) + 100) + 100) + 100) + 100
#     = 500



#solution Number 2
n = int(input("Enter the value: "))
f = lambda x: f(x-1)+100 if x > 0 else 0
print(f(n))



#Last Solution 

def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + 100

# Test the function
n = int(input("Enter the value of n: "))
result = f(n)
print(f"f({n}) = {result}")
