from casting.actor import Actor
from casting.point import Point
from constants import *

class PlayerShip(Actor):
    def __init__(self, body, animation, debug = False) -> None:
        super().__init__(debug)
        self._body = body
        self._animation = animation
    
    def get_animation(self):
        return self._animation
    
    def get_body(self):
        return self._body
    
    def move_next(self):
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)
    
    def swing_backwards(self):
        """ Ship moves to the left or backwards on the screen"""
        velocity = Point(-SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def swing_forwards(self):
        velocity = Point(SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def swing_up(self):
        velocity = Point(0, -SHIP_VELOCITY)
        self._body.set_velocity(velocity)
    
    def swing_down(self):
        velocity = Point(0, SHIP_VELOCITY)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)