class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        s = "Rectangle(width={}, height={})".format(self.width, self.height)
        return s

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2*self.width + 2*self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** .5
        return diagonal

    def get_picture(self):
        if (self.width > 50) or (self.height > 50):
            return "Too big for picture."
        picture = ('*'*self.width + '\n') * self.height
        return picture

    def get_amount_inside(self, shape):
        times = int(self.get_area() / shape.get_area())
        return times


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        s = "Square(side={})".format(self.width)
        return s

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height
        
    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
