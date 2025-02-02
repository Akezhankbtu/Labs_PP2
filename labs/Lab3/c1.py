class String:
    def __init__(self):
        self.txt = ""

    def getstr(self):
        x = input("enter: ")
        self.txt += x
    
    def printstr(self):
        print(self.txt.upper())

a = String()
a.getstr()
a.printstr()
