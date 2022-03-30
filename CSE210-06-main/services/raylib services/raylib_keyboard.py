import pyray
import raylib
from services.keyboard_service import KeyboardService

class RaylibkeyBoardService(KeyboardService):
    
    def __init__(self):
        self._keys = {}
        self._keys["a"] = pyray.KEY_A
        self._keys["d"] = pyray.KEY_D
        self._keys["w"] = pyray.KEY_W
        self._keys["s"] = pyray.KEY_S
        self._keys["j"] = pyray.KEY_J
        self._keys["l"] = pyray.KEY_L
        self._keys["i"] = pyray.KEY_I
        self._keys["K"] = pyray.KEY_K
        self._keys["space"] = pyray.KEY_SPACE
        self._keys["shift"] = pyray.KEY_SHIFT
        
    def is_key_down(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_down(raylib_key)
    
    def is_key_up(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_up(raylib_key)
    
    def is_key_pressed(self,key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_pressed(raylib_key)
    
    def is_key_released(self, key):
        raylib_key = self.keys[key.lower()]
        return pyray.is_key_released(raylib_key)