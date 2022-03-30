"""
ANIMATION

gets all of the prospects needed for an animation to take place
we don't need the last function quite just yet. 
"""
import time
from constants import *
# import images also

class Animation:

    def __init__(self, delay = 0, rate = 6, images = 0) -> None:
        self._delay = delay
        self._rate = rate
        self.images = images
        self._index = 0
        self._frame = 0
        self._start = time.time()
    
    def get_delay(self):
        return self._delay
    
    def set_delay(self, new_delay):
        self._delay = new_delay
        

    def get_rate(self):
        return self._rate
    
    def set_rate(self, new_rate):
        self._rate = new_rate 
        

    def get_images(self):
        return self.images
    
    def set_images(self, new_images):
        self.images = new_images
        

    def get_next_image(self):
        pass