class Sound:
    def __init__(self, sound_file, volume = 1, repeat = False) -> None:
        self._sound_file = sound_file
        self._volume = volume
        self._repeated = repeat
    
    def get_filename(self):
        return self._sound_file
    
    def get_volume(self):
        return self._volume
    
    def is_repeated(self):
        return self._repeated
    