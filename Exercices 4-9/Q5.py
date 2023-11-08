class IOString():
    def get_String(self):
        self.s = input("Enter a string: ")
        
    def print_String(self):
        print(self.s.upper())
        
XX = IOString()
XX.get_String()
XX.print_String()    


