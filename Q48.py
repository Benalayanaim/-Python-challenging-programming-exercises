class Recatangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


rect = Recatangle(2, 4)
print(rect.area())    
