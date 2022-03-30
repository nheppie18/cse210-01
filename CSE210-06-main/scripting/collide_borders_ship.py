'''
What happens if the ship hits the side.
'''

from constants import *
from casting.sound import Sound
from scripting.action import Action


class CollideBordersShipAction(Action):
    def __init__(self, physics_service, audio_service) -> None:
        self._physics_service = physics_service
        self._audio_service = audio_service
    
    def execute(self, cast, script, callback):
        player_ship = cast.get_first_actor(SHIP_GROUP)
        body = player_ship.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        hit_sound = Sound(HIT_SOUND)
        game_over_sound = Sound(GAME_OVER_SOUND) 

        if x < FIELD_LEFT :
            player_ship.swing_forwards()
            self._audio_service.play_sound(hit_sound)

        elif x >= (FIELD_RIGHT - SHIP_WIDTH) :
            player_ship.swing_backwards()
            self._audio_service.play_sound(hit_sound)
        
        if y < FIELD_TOP :
            player_ship.swing_down()
            self._audio_service.play_sound(hit_sound)
        
        elif y >= (FIELD_BOTTOM - SHIP_WIDTH):
            player_ship.swing_up()
            self._audio_service.play_sound(hit_sound)
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life("Border")

            if stats.get_lives() == 0 :
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(game_over_sound)