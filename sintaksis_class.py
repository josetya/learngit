#sintaksis_class

class triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def calculate_area (self) :
        return self.height * self.base / 2
    def get_info(self):
        print ('information height = ',self.height,' base = ',self.base)
triangle = triangle(5,3)
print (triangle.calculate_area())

triangle.get_info()