from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("Enter the Length: "))
        self.breadth=int(input("Enter the Breadth: "))
    def get_area(self):
        print("Area is ",self.length*self.breadth)
    def get_perimeter(self):
        print("Perimeter is",(self.length+self.breadth)*2)
class Square(Shape):
    def __init__(self):
        self.side = int(input("Enter the Side: "))
    def get_area(self):
        print("Area is ",self.side*self.side)
    def get_perimeter(self):
        print("Perimeter is ", self.side *4)
r=Rectangle()
r.get_area()
r.get_perimeter()
s=Square()
s.get_area()
s.get_perimeter()