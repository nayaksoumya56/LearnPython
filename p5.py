# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters
class myclass:
    s=None
    def __init__ (self):
        self.s="default string"

    def getString(self):
        self.s=input("Enter a string : ")
    def printString(self):
        print(self.s.upper())

obj = myclass()
obj.getString()
obj.printString()
