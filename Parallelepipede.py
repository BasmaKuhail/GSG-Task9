import Rectangle


class Parallelepiped(Rectangle.Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        self.display()

    def volume(self):
        return self.height * super().area()

    def display(self):
        super().display()
        print("height:", self.height)
        print("volume:", self.volume())


prll = Parallelepiped(4, 3, 20)
