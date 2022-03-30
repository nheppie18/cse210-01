from casting.actor import Actor
from casting.point import Point
from constants import *

class EnemyShip(Actor):
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
    
    def move_left(self) :
        velocity = Point(-SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)
    