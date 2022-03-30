"""
Scene Manager
Shuffles through each scene as necessary

"""
from cgitb import text
from random import Random, randint, random
from casting.point import Point
from scripting.release_devices_action import ReleaseDevicesAction
from scripting.stats import Stats
from casting.text import Text
from casting.player_ship import PlayerShip
from casting.image import Image
from casting.body import Body
from casting.label import Label
from scripting.load_assets_action import LoadAssetsAction
from casting.enemy_ship import EnemyShip
from scripting.timed_change_scene_action import TimedChangeSceneAction
from services.raylib_services.raylib_keyboard import RaylibKeyboardService
from services.raylib_services.raylib_video_service import RaylibVideoService
from services.raylib_services.raylib_audio import RaylibAudioService
from services.raylib_services.raylib_physics import RaylibPhysicsService
from scripting.draw_HUD_action import DrawHudAction
from scripting.draw_enemy_ship_action import DrawEnemyShipAction
from scripting.start_drawing_action import StartDrawingAction
from scripting.draw_lasers_action import DrawLaserAction
from scripting.control_ship_action import ControlShipAction
from scripting.collide_borders_ship import CollideBordersShip
from scripting.collide_enemy_laser import CollideEnemyLaser
from scripting.collide_enemy_ship import CollideEnemyShip
from scripting.draw_ship_action import DrawShipAction
from scripting.initialize_devices_action import InitializeDevicesAction
from scripting.end_drawing_action import EndDrawingAction
from scripting.draw_dialog_action import DrawDialogAction
from scripting.unload_assets_action import UnloadAssetsAction
from scripting.move_ship_action import MovePlayerShipAction
from scripting.change_scene_action import ChangeSceneAction
from scripting.move_enemy_ship_action import MoveEnemyShipAction
from constants import *

class SceneManager:
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    KEYBOARD_SERVICE = RaylibKeyboardService()
    CONTROL_SHIP_ACTION = ControlShipAction(KEYBOARD_SERVICE)
    PHYSICS_SERVICE = RaylibPhysicsService()
    AUDIO_SERVICE = RaylibAudioService()
    PLAYER_SHIP = None
    HEAVY_ENEMY_SHIP = None
    MEDIUM_ENEMY_SHIP = None
    LIGHT_ENEMY_SHIP = None 

    COLLIDE_ENEMY_LASER_ACTION = CollideEnemyLaser(PHYSICS_SERVICE, VIDEO_SERVICE)
    # COLLIDE_ENEMY_SHIP_ACTION = CollideShipsAction(PHYSICS_SERVICE, VIDEO_SERVICE)
    # COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, VIDEO_SERVICE)
    DRAW_LASERS_ACTION = DrawLaserAction(VIDEO_SERVICE, PLAYER_SHIP)
    DRAW_HEAVY_ENEMY_LASERS_ACTION = DrawLaserAction(VIDEO_SERVICE, HEAVY_ENEMY_SHIP)
    DRAW_MEDIUM_ENEMY_LASERS_ACTION = DrawLaserAction(VIDEO_SERVICE, MEDIUM_ENEMY_SHIP)
    DRAW_LIGHT_ENEMY_LASERS_ACTION = DrawLaserAction(VIDEO_SERVICE, LIGHT_ENEMY_SHIP)
    DRAW_SHIP_ACTION = DrawShipAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_ENEMY_SHIP_ACTION = DrawEnemyShipAction(VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_SHIP_ACTION = MovePlayerShipAction()
    MOVE_HEAVY_ENEMY_SHIP_ACTION = MoveEnemyShipAction(HEAVY_ENEMY_SHIP_GROUP)
    MOVE_MEDIUM_ENEMY_SHIP_ACTION = MoveEnemyShipAction(MEDIUM_ENEMY_SHIP_GROUP)
    MOVE_LIGHT_ENEMY_SHIP_ACTION = MoveEnemyShipAction(LIGHT_ENEMY_SHIP_GROUP)

    


    def __init__(self) -> None:
        pass
        

    """
    Casting Methods
    """
    def _add_player_ship(self, cast):
        cast.clear_actors(SHIP_GROUP)
        position = Point(CENTER_X, CENTER_Y)
        size = Point(SHIP_WIDTH, SHIP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(SHIP_IMAGE)
        self.PLAYER_SHIP = PlayerShip(body, image, False)
        cast.add_actor(SHIP_GROUP, self.PLAYER_SHIP)
    
    def _add_enemy_ships(self, cast, heavy_ships, medium_ships, light_ships):
        cast.clear_actors(HEAVY_ENEMY_SHIP_GROUP)
        cast.clear_actors(MEDIUM_ENEMY_SHIP_GROUP)
        cast.clear_actors(LIGHT_ENEMY_SHIP_GROUP)

        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        

        for heavy_enemy_ship_count in range(0, heavy_ships) :
            position = Point(MAX_X + 1, Random.randint(0, MAX_Y - 1))
            size = Point(SHIP_WIDTH, SHIP_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(HEAVY_ENEMY_SHIP_IMAGE)
            self.HEAVY_ENEMY_SHIP = EnemyShip(body, image, False)
            cast.add_actor(HEAVY_ENEMY_SHIP_GROUP, self.HEAVY_ENEMY_SHIP)
        
        for medium_enemy_ship_count in range(0, medium_ships) :
            position = Point(MAX_X + 1, Random.randint(0, MAX_Y - 1))
            size = Point(SHIP_WIDTH, SHIP_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(MEDIUM_ENEMY_SHIP_IMAGE)
            self.HEAVY_ENEMY_SHIP = EnemyShip(body, image, False)
            cast.add_actor(MEDIUM_ENEMY_SHIP_GROUP, self.HEAVY_ENEMY_SHIP)
        
        for light_enemy_ship_count in range(0, light_ships) :
            position = Point(MAX_X + 1, Random.randint(0, MAX_Y - 1))
            size = Point(SHIP_WIDTH, SHIP_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(MEDIUM_ENEMY_SHIP_IMAGE)
            self.LIGHT_ENEMY_SHIP = EnemyShip(body, image, False)
            cast.add_actor(LIGHT_ENEMY_SHIP_GROUP, self.LIGHT_ENEMY_SHIP)
    
    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP) 
        text = Text(LEVEL_FORMAT,FONT_FILE, ALIGN_CENTER, FONT_SMALL)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)
    
    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, ALIGN_LEFT, FONT_SMALL)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)
    
    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, ALIGN_RIGHT, FONT_FILE, FONT_SMALL)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)
    
    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)
    
    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, ALIGN_CENTER, FONT_SMALL)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)
    
    """
    Scripting Methods
    
    """

    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_SHIP_ACTION)
        script.add_action(OUTPUT, self.DRAW_SHIP_ACTION)
        script.add_action(OUTPUT, self.DRAW_LASERS_ACTION)
        script.add_action(OUTPUT, self.DRAW_ENEMY_SHIP_ACTION)
        script.add_action(OUTPUT, self.DRAW_HEAVY_ENEMY_LASERS_ACTION)
        script.add_action(OUTPUT, self.DRAW_MEDIUM_ENEMY_LASERS_ACTION)
        script.add_action(OUTPUT, self.DRAW_LIGHT_ENEMY_LASERS_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)
    
    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
    
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION) 
        script.add_action(UPDATE, self.MOVE_HEAVY_ENEMY_SHIP_ACTION)
        script.add_action(UPDATE, self.MOVE_MEDIUM_ENEMY_SHIP_ACTION)
        script.add_action(UPDATE, self.MOVE_LIGHT_ENEMY_SHIP_ACTION)
        script.add_action(UPDATE, )

    """
    Prepare the Game
    """
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_player_ship(cast)
        self._add_enemy_ships(cast, 0, 2, 6)
        self._add_dialog(cast, "PRESS ENTER TO PLAY")

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
    
    def _prepare_next_level(self, cast, script):
        self._add_player_ship(cast)
        self._add_enemy_ships(cast, LEVEL_1_AMOUNT[0], LEVEL_1_AMOUNT[1], LEVEL_1_AMOUNT[2])
        self._add_dialog(cast, "PREPARE TO WRECK")

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
    
    def _prepare_try_again(self, cast, script):
        self._add_player_ship(cast)
        self._add_enemy_ships(cast, LEVEL_2_AMOUNT[0], LEVEL_2_AMOUNT[1], LEVEL_2_AMOUNT[2])
        self._add_dialog(cast, "PREPARE TO WRECK")

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)


    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME :
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL :
            self._prepare_next_level(cast, script)
        