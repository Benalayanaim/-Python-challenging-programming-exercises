#Using For Loops
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 !=0:
        print(i, end=',')

print("\b")

#After the loop completes, the code print("\b") is intended to erase the trailing comma that would be present at the end of the line. However,
#  it doesn't work as expected because "\b" is a backspace character that moves the cursor back one position, 
# but it doesn't remove characters that have already been printed. As a result, it may not have the desired effect of erasing the comma.

#You can simply remove the print("\b") line, and the code will still function correctly to print the desired numbers without the trailing comma.



#Using generators and list comprehension
print(*(i for i in range(2000, 3201) if i % 7 ==0 and i % 5 != 0), sep=",")