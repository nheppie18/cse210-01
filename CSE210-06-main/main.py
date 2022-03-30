from directing.director import Director
from constants import *
from directing.scene_manager import SceneManager

def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

main()