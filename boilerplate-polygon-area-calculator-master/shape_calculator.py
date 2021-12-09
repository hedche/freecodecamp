class Rectangle:
    
    #Using init here to assign the width and height variables being used in this class
    def __init__(self, width, height):
      self.width = width
      self.height = height

    #Using string interpolation, printing out the desired string based on the project requirements
    def __str__(self):
      return f'Rectangle(width={self.width}, height={self.height})'


    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return (self.width * self.height)

    #Gets the perimiter 
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    #Get the diagonal based on pythagoras
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    #This will return the rectangle/square based on width and height in asterisks.
    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        picture = (("*" * self.width) + "\n") * self.height
        return picture

    #Method to get amount of times 'shape' will fit into the area of the Rectangle/Square
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

    

#Square class that inherits all methods from Rectangle class
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side