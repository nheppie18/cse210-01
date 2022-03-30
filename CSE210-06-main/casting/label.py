from distutils.log import debug
from casting.actor import Actor

class Label(Actor):
    
    def __init__(self, text, position, debug = False):
        super().__init__(debug=False)
        self._text = text
        self._position = position
    
    def get_position(self):
        return self._position

    def get_text(self):
        return self._text

