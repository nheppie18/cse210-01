from pyray import poll_input_events
from constants import *
from casting.actor import Actor

class Stats(Actor):

    def __init__(self, debug=False):
        super().__init__(debug)
        self._level = 1
        self._lives = DEFAULT_LIVES 
        self._score = 0
    
    def add_life(self):
        if self._lives < MAXIMUM_LIVES:
            self._lives += 2
    
    def add_points(self, points):
        self._score += points
    
    def get_level(self):
        return self._level
    
    def get_lives(self):
        return self._lives
    
    def get_score(self):
        return self._score
    
    def lose_life(self, type):
        if type == "Heavy" and self._lives > 0 :
            self._lives -= LASER_HEAVY_DAMAGE
        
        elif type == "Medium" and self._lives > 0 :
            self._lives -= LASER_MEDIUM_DAMAGE 
        
        elif type == "Light" and self._lives > 0 :
            self._lives -= LASER_LIGHT_DAMAGE
        
        elif type == "Border" and self._lives > 0 :
            self._lives -= 2
    
    def next_level(self):
        self._level += 1
    
    def set_level(self, level):
        self._level = level
        assert(level > 0)
    
    def reset(self) :
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0
    
