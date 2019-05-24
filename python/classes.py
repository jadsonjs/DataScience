#
# https://docs.python.org/3/tutorial/
#
# to execute this file type:  "python3 classes.py" on linux or macoc terminal
#

"""My Class in Python """
class Square:
    
    side = 10

    # class constructor 
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side;



s = Square(20)

print ( s.area() )
