a = input()
total,tmp = 0,str()  #initialing an integr and empty string 

for i in range(4):
    
    tmp += a          #concatenating 'a  to 'tmp'
    total +=int(tmp)  #converting string type to integer type

print(total)

#how work when i Execute 
#Let's walk through the code with the input 5:

#Initialize total to 0 and tmp to an empty string.
#Enter the loop with i ranging from 0 to 3.
#In the first iteration, concatenate tmp with the input digit, resulting in tmp = '5'.
#Add the integer value of tmp to total, making total = 5.
#In the second iteration, concatenate tmp with the input digit again, resulting in tmp = '55'.
#Add the integer value of tmp to total, making total = 5 + 55 = 60.
#Repeat the process for the third and fourth iterations.
#Print the final value of total, which is 5 + 55 + 555 + 5555 = 6170.
#So, if you input 5, the output should be 6170.



#Solution number 2
def digitvalue(string_digit):
    return sum(int(string_digit * n) for n in range(1, 5))

inp = input('please enter a digit: ')
print(digitvalue(inp)) 