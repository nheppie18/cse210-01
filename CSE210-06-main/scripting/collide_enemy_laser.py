from scripting.action import Action
from casting.sound import Sound
from constants import *


class CollideEnemyLaser(Action):
    def __init__(self, physics_service, audio_service) -> None:
        self._physics_service = physics_service
        self._audio_service = audio_service
    
    def execute(self, cast, script, callback):
        player_ship = cast.get_first_actor(SHIP_GROUP)
        lasers = cast.get_actors(LASER_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for laser in lasers :
            player_ship_body = player_ship.get_body()
            laser_body = laser.get_body()
            
            
            # Need to determine which ship fired the shot and how much damage is done
            if self._physics_service.has_collided(player_ship_body, laser_body) :
                 sound = Sound(HIT_SOUND)
                 self._audio_service.play_sound(sound)
                 damage = laser.get_damage()
                 stats.remove_life(damage)
                 cast.remove_actor(LASER_GROUP, laser)