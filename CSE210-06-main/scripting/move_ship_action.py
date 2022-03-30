from constants import * 
from casting.point import Point
from scripting.action import Action

class MovePlayerShipAction(Action):
    def __init__(self) -> None:
        pass

    def execute(self, cast, script, callback):
        ship = cast.get_fisrt_actor(SHIP_GROUP)
        body = ship.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

        position = position.add(velocity)

        if x < 0 :
            position = Point(0, position.get_y())
        
        elif x > (SCREEN_WIDTH - SHIP_WIDTH) :
            position = Point(SCREEN_WIDTH - SHIP_WIDTH, position.get_y())
        
        if y < 0 :
            position = Point(position.get_x(), 0)
        
        elif y > (SCREEN_HEIGHT - SHIP_HEIGHT) :
            position = Point(position.get_x(), (SCREEN_HEIGHT - SHIP_HEIGHT))
        