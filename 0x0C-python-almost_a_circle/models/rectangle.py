#!/usr/bin/python3
    """
    Write the class Rectangle that 
    inherits from Base
    """
from models.base import Base


class Rectangle(Base): # class Rectangle inherits from class Base
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = Width
        self.height = height
        self.x = x
        self.y = y

        def width(self):  # width getter
        return self.__width

    def width(self, value):  # width setter
        if value is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def height(self):  # height getter
        return self.__height

    def height(self, value):
        if value is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def x(self):  # x getter
        return self.__x

    def x(self, value):
        if value is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def y(self):  # y getter
        return self.__y

    def y(self, value):
        if value is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):  # returns area
        return self.width * self.height

    def display(self):
        for col in range(self.y):
            print()
        for y_axis in range(self.height):
            for x_axis in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        '''
        Allows for variadic args
        '''
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''
       Pull the parameters out in
       the function as a dictionary
        '''
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width}

    def __str__(self):
        '''
        String representation
        '''
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height))
