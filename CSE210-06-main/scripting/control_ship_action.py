from scripting.action import Action
from constants import *

class ControlShipAction(Action):
    def __init__(self, keyboard_service) -> None:
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        ship1 = cast.get_first_actor("player")

        if self._keyboard_service.is_key_down(MOVE_BACKWARDS_P1) :
            ship1.swing_backwards()
        
        elif self._keyboard_service.is_key_down(MOVE_FORWARDS_P1) :
            ship1.swing_forwards()

        elif self._keyboard_service.is_key_down(MOVE_UP_P1) :
            ship1.swing_up()
        
        elif self._keyboard_service.is_key_down(MOVE_DOWN_P1) :
            ship1.swing_down()

        else: 
            ship1.stop_moving()
