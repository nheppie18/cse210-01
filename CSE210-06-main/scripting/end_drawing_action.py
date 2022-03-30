from scripting.action import Action

class EndDrawingAction(Action):

    def __init__(self, video_service) -> None:
        self._video_service = video_service
    
    def execute(self, cast, script, callback):
        self._video_service.flush_buffer()