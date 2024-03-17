s = input()
u = s.encode('utf-8')
print(u)



#Another Solution

# Read an ASCII string from the user
ascii_string = input("Enter an ASCII string: ")

# Convert the ASCII string to a Unicode string encoded with UTF-8
unicode_string = ascii_string.encode('utf-8')

# Display the result
print("Original ASCII String:", ascii_string)
print("UTF-8 Encoded Unicode String:", unicode_string.decode('utf-8'))
