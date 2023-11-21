#It looks like you are trying to implement a program that takes directional commands (UP, DOWN, LEFT, RIGHT) 
#with associated units of movement and calculates the Euclidean distance based on the movements. However,
# there are a few issues in your code:

#The input().split line is missing parentheses. It should be input().split(). Currently,
#you are not actually calling the split method, and s remains a reference to the method itself rather than the result of the split operation.

#The conditions for checking the commands are case-sensitive. You are checking for 'Right' instead of 'RIGHT'.
# Make sure the case matches the input.

#The distance calculation should be inside the loop, so it accumulates the distance after each move.

import  math

x,y = 0,0
while True:
    s = input().split()
    if not s:
        break
    if s[0]=='UP':                  # s[0] indicates command
        x-=int(s[1])                # s[1] indicates unit of move
    if s[0]=='DOWN':
        x+=int(s[1])
    if s[0]=='LEFT':
        y-=int(s[1])
    if s[0]=='RIGHT':
        y+=int(s[1])
                                    # N**P means N^P
dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)

#Example for input and undrestand the ouput 


#If you input the following commands:

#UP 5
#RIGHT 3
#DOWN 2
#LEFT 1
#The program should calculate the Euclidean distance based on these movements. Let's manually calculate it:

#Move UP by 5 units: (x, y) = (0 - 5, 0) => (x, y) = (-5, 0)
#Move RIGHT by 3 units: (x, y) = (-5, 0 + 3) => (x, y) = (-5, 3)
#Move DOWN by 2 units: (x, y) = (-5 + 2, 3) => (x, y) = (-3, 3)
#Move LEFT by 1 unit: (x, y) = (-3, 3 - 1) => (x, y) = (-3, 2)
#Now, calculate the Euclidean distance: dist = round(math.sqrt((-3)**2 + 2**2)), 
# which simplifies to dist = round(math.sqrt(9 + 4)), and finally, dist = round(math.sqrt(13)).
#  The rounded value of the square root of 13 is approximately 4.

#So, the program should output 4 when you press Enter to end the input.



#Another Solution
'''Solution by: pratikb0501
'''

from math import sqrt
lst = []
position = [0,0]
while True:
    a = input()
    if not a:
        break                     # Break the loop if an empty input is encountered 
    lst.append(a)                   # Add the input string to the list
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))

#In this case, strip('UP ') removes the characters 'U', 'P', and space from both ends of the string "UP 5". The resulting string, "5", can then be converted to an integer.

#It's worth noting that strip() removes characters from both ends of the string until it encounters a character that is not in the specified argument. If no argument is provided, strip() removes leading and trailing whitespaces by default.

#So, in the given solution, i.strip('UP ') removes 'UP ' from the beginning of the string i when the command is 'UP', and similarly for the other directions. This way, the solution extracts the numeric part of the command (e.g., the distance to move) and updates the position accordingly.



#print(round(sqrt(position[1] ** 2 + position[0] ** 2)))

#position[1] ** 2 + position[0] ** 2 calculates the sum of the squares of the x and y coordinates of the position.
#sqrt() calculates the square root of that sum.
#round() then rounds the result to the nearest integer.
#This rounding ensures that the final output is an integer representing the Euclidean distance.
#  If you remove the round() function, the result would be a floating-point number representing the exact
#  Euclidean distance without rounding. In this context, rounding to the nearest integer is 
# common when dealing with distances in a grid or similar scenarios where only whole units make sense.







