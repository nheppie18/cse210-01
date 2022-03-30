"""
This essentially makes a detectable hitbox for the given object. 

"""
from casting.point import Point 
from casting.hitbox import HitBox

class Body:
    def __init__(self, size = Point(), position = Point(), velocity = Point() ) -> None:
        self._size = size
        self._position = position
        self._velocity = velocity
    
    def get_size(self):
        """
        Get's the body's position

        RTRN: Size (Point())
        """
        return self._size
    
    def get_position(self):
        """
        Get's the Position of the body
        
        RTRN: Position (Point())
        """
        return self._position
    
    def get_velocity(self):
        """
        Get's the velocity of the body

        RTRN: Velocity (Point())
        
        """
        return self._velocity
    
    def get_rectangle(self):
        """
        Get's a Hitbox aroundt he body

        RTRN: Hitbox Instance
        
        """
        return HitBox(self._position, self._size)
    
    def set_size(self, size: Point) -> None:
        """
        Used to set the size of a body

        ARGS: size (Point())
        
        """
        self._size = size
    
    def set_position(self, position: Point) -> None:
        """
        Used to set the position of a body

        ARGS: size(Point())
        """

        self._position = position
    
    def set_velocity(self, velocity: Point) -> None:
        """
        Used to modify the velocity of a body

        ARGS: velocity (Point())
        """

        self._velocity = velocity
    

