class KeyboardService:
    
    def is_key_down(self, key):
        raise NotImplementedError("not implemented in base class")
    
    def is_key_up(self, key):
        raise NotImplementedError("not implemented in base class")
    
    def is_key_pressed(self,key):
        raise NotImplementedError("not implemented in base class")
    
    def is_key_released(self,key):
        raise NotImplementedError("not implemented in base class")