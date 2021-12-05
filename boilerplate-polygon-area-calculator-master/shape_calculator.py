class Rectangle:
    def __init__(self, width, height):
        set_width = self.width
        set_height = self.height

    def get_area(self):
        return self.width * self.height 

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

class Square(Rectangle):
    def __init__(self):
        square_height = 