def divide():
    return 5/0

try:
    divide()

except ZeroDivisionError as ze:
    print("why on earth you are dividing a number by zero !")

except:
    print("Any other exception")        