#!/usr/bin/python3
"""My square class definition"""


class square():
    """My square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Create a new square class instance
        Args:
            width (int): the square width
            height (int): the square height"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ calculates and returns the permiter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Prints square area and permiter"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
