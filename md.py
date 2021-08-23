class area():
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area = length * width
        print (f"Your area is {self.area}square foot")

class circumference():
    def __init__ (self,radius):
        self.radius = radius
        self.circ = 2 * radius * 3.14
        print (f'The circumference of your circle is {self.circ}feet')