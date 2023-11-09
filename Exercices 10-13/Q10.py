word = input().split()
for i in word:
    if word.count(i) >1:   #count function returns total repeatation of an element that is send as argument 
        word.remove(i)     #removes exactly one element per call 

word.sort()
print(" ".join(word))


#solution number 2
word =  input("").split()
[word.remove(i) for i in word if word.count(i) > 1] #removal operation with comprehension method
word.sort()
print(" ".join(word))


#solution number 3
word = sorted(list(set(input().split()))) # input strings splits => converting into set() to store unique 
                                          # elemnt => converting into list to be apply sort

print(" ".join(word))  

