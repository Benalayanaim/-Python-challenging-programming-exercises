class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) +1):
            yield i * 7


for i in MyGen().by_seven(int(input('Please enter a number: '))):
    print(i)




#Another Solution

class Divisible:
    def by_seven(self, n):
        for number in range(1, n+ 1):
            if number % 7 == 0:
                yield number

divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number: ")))
for number in generator:
    print(number)

