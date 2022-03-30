from scripting.action import Action

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service) -> None:
        self._audio_service = audio_service
        self._video_service = video_service
    
    def execute(self, cast, script, callback):
        self._audio_service.load_sounds("CSE210-06/assets/Sounds")
        self._audio_service.load_fonts("CSE210-06/assets/Fonts")
        self._audio_service.load_images("CSE210-06/assets/Images")
        