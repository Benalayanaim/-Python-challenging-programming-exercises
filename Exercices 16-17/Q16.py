lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))

#Example for input and output with Explaination 

#Explanation:

#1 is odd, so its square is 1.
#3 is odd, so its square is 9.
#5 is odd, so its square is 25.
#7 is odd, so its square is 49.
#9 is odd, so its square is 81.
#The program filters out the even numbers and squares the odd numbers, then joins them into a comma-separated string for the final output.




#another solution 
#square odd no 

lst = input().split(',')  #splits in comma postion and set up in list

seq = []
lst = [int(i) for i in lst] #converts string to integer
for i in lst:
    if i%2 !=0:
        i = i*i
        seq.append(i)

seq = [str(i) for i in seq ] #All the integres are convertes to string to be able to aplly join operation 
print(",".join(seq))        