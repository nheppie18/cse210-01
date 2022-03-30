from constants import * 
from scripting.action import Action

class MoveEnemyShipAction(Action):
    
    def __init__(self, group) -> None:
        self._group = group
    
    def execute(self, cast, script, callback):
        for ship in range(0, len(cast.get_actors(self._group))):
            enemy_ship = cast.get_actor_by_index(self._group, ship)
            body = enemy_ship.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
    