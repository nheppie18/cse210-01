from constants import * 


class Text: 
    def __init__(self, value, fontfile = FONT_FILE, alignment = ALIGN_LEFT, size = FONT_LARGE) -> None:
        self._value = value
        self._fontfile = fontfile
        self._size = size
        self._alignment = alignment
    
    def get_alignment(self):
        return self._alignment
    
    def get_value(self):
        return self._value
    
    def get_fontfile(self):
        return self._fontfile
    
    def get_size(self):
        return self._size
    
    def set_value(self, value):
        self._value = value