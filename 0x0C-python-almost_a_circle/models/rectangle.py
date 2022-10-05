#!/usr/bin/python3
"""
    creating a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """  rectangle class definition inheriting Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class instantiation """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ x setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ evaluates area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ display # representation of the rectngle"""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))
    
    def __str__(self):
        """ informal representation of Rectangle class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update(self, *args, **kwargs):
        """ update arguments via args"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ dictionary representation of a square"""
        rect_dict = {}
        rect_dict["id"] = self.id
        rect_dict["width"] = self.width
        rect_dict["height"] = self.height
        rect_dict["x"] = self.x
        rect_dict["y"] = self.y
        return rect_dict





