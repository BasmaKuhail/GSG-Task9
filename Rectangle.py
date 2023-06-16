class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        #self.display()

    def perimeter(self):
        square_p = self.length**2 + self.width**2
        p = square_p ** (1/2)
        return p

    def area(self):
        return self.length * self.width

    def display(self):
        print("length:", self.length)
        print("width:", self.width)
        print("perimeter", self.perimeter())
        print("area", self.area())



