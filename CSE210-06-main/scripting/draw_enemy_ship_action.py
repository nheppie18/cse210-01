"""
This class will draw the enemy ships

"""
from constants import *
from scripting.action import Action


class DrawEnemyShipAction(Action):
    def __init__(self, video_service) -> None:
        self._video_service = video_service

    def execute(self, cast, script, callback):
        heavy_enemy_ships = cast.get_actors(HEAVY_ENEMY_SHIP_GROUP)
        medium_enemy_ships = cast.get_actors(MEDIUM_ENEMY_SHIP_GROUP)
        light_enemy_ships = cast.get_actors(LIGHT_ENEMY_SHIP_GROUP)

        for heavy_enemy_ship in heavy_enemy_ships :
            body = heavy_enemy_ship.get_body()

            animation = heavy_enemy_ship.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
            
        for medium_enemy_ship in medium_enemy_ships :
            body = medium_enemy_ship.get_body()
            
            animation = medium_enemy_ship.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

        
        for light_enemy_ship in light_enemy_ships :
            body = light_enemy_ship.get_body()

            animation = light_enemy_ship.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)