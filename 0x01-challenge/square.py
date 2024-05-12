#!/usr/bin/python3

class square():
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if value > 0:
                   setattr(self, key, value)
            if "height" in kwargs.items() and "width" not in kwargs.items():
                self.width = self.height
            if "width" in kwargs.items() and "height" not in kwargs.items():
                self.height = self.width
        self.height = self.width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
