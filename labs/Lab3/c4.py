import math

class coord:
    def init(s, x, y):
        s.x = x
        s.y = y
    
    def move(s, x, y):
        s.x = x
        s.y = y
    
    def dist(s, other):
        return math.sqrt(((s.x - other.x) **2) + ((s.y - other.y)**2))
    
    def show(s):
        print("x:", s.x, ", y:", s.y)


point = coord(int(input("Enter x value: ")), int(input("Enter y value: ")))

while True:
    a = str(input("\nPrint 'q' if you want to quit \nWhat do you want? \nshow \nmove \ndist \n\n"))
    
    if a == 'q':
        break
    elif a == "show":
        point.show()
    elif a == "move":
        x1 = int(input("enter new x value: "))
        y1 = int(input("enter new y value: "))
        point.move(x1, y1)
    elif a == "dist":
        x2 = int(input("Enter x value of second point: "))
        y2 = int(input("Enter y value of second point: "))
        other = coord(x2,y2)
        print(f"dist: {point.dist(other):.2f}")