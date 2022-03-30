from constants import *
from scripting.action import Action

class DrawLaserAction(Action):
    def __init__(self, video_service, ship) -> None:
        self._video_service = video_service
        self._ship = ship
    
    def execute(self, cast, script, callback):
        lasers = cast.get_actors(LASER_GROUP)
        
        for laser in lasers :
            body = laser.get_body()

            if laser.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle)
            
            image = laser.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
            
            