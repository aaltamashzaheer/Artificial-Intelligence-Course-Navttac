class shape():
    def calculate_area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def calc_area(self):
        return 3.14*(self.radius**2)

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def calc_area(self):
        return self.length* self.breadth

userinput= input("Press 1 to Calculate Area of a Circle\nPress 2 to Calculate Area of a Rectangle\nPress 3 to Exit\n")

if userinput == "1":
    radius= float(input("Enter Radius: "))
    circle_instance = circle(radius)
    area = circle_instance.calc_area()
    print("Area of a circle is: ",area)
elif userinput == "2":
    length = float(input("Enter Length: "))
    breadth = float(input("Enter Breadth: "))
    AreaOfRectangle = rectangle(length,breadth)
    print("Area of a rectangle is: ",AreaOfRectangle.calc_area())
elif userinput == "3":
    print("Exiting...")
    exit()
else:
    print("Invalid Input")
    