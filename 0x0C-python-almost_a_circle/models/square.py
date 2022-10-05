#!/usr/bin/python3
"""
    The Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ definition of class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """class initialization with attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """ informal representation of Rectangle class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ update arguments via args"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ dictionary representation of a square"""
        sqr_dict = {}
        sqr_dict["id"] = self.id
        sqr_dict["size"] = self.size
        sqr_dict["x"] = self.x
        sqr_dict["y"] = self.y
        return sqr_dict
