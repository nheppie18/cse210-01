"""
Director:
Manages the game, starts it up 

"""
from directing.scene_manager import SceneManager
from scripting.script import Script
from casting.cast import Cast
from constants import *

class Director: 
    def __init__(self, video_service) -> None:
        self._video_service = video_service
        self._cast = Cast()
        self._scripting = Script()
        self._scene_manager = SceneManager()

    def on_next(self, scene):
        self._scene_manager.prepare_scene(scene, self._cast, self._scripting)

    def start_game(self, ):
        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)
    
    def _execute_actions(self, group):
        """
        Calls execute for each action in any group
        
        Args: 
            group (string): The action group name
            cast (Cast): Cast of all actors
            script(Script): The script of all the actions
        
        """ 
        actions = self._scripting.get_actions(group)
        for action in actions :
            action.execute(self._cast, self._script, self)
