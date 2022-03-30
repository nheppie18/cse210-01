class Point: 
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
    
    def get_point(self):
        return Point(self.x, self.y)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def add(self, other):
        x = self.x + other.get_x()
        y = self.y + other.get_y()
    
    def equals(self, other):
        return self.x == other.get_x() and self.y == other.get_y()
    
    def equals_box(self, other):
        other_x = other.get_x()
        other_y = other.get_y()

        return self.x == other_x + 5 or self.x == other_x - 5 and self.y == other_y + 5 or self.y == other_y - 5
    