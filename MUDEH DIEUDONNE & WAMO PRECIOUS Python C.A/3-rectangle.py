class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.__width, self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    # Testing the Rectangle class
rect1 = Rectangle()
print(rect1)                     # Output: Rectangle(width=0, height=0)
print(rect1.area())              # Output: 0
print(rect1.perimeter())         # Output: 0
rect1.width = 5
print(rect1)                     # Output: Rectangle(width=5, height=0)
print(rect1.area())              # Output: 0
print(rect1.perimeter())         # Output: 10
rect2 = Rectangle(4, 6)
print(rect2)                     # Output: Rectangle(width=4, height=6)
print(rect2.area())              # Output: 24
print(rect2.perimeter())         # Output: 22  

                                          
                                          