"""
This make a rectangle around the given object.
Essentially detecting it's size

"""
from casting.point import Point

class HitBox: 
    def __init__(self, position, size) -> None:
        self.position = Point()
        self.size = Point()
    
    def get_position(self):
        return self.position
    
    def get_size(self):
        return self.size