class PhysicsService: 

    def has_collided(self, subject, agent):
        raise NotImplementedError("Error Collision not detected due to implementation")
    
    def is_above(self, subject, agent) :
        raise NotImplementedError("Error not implemented in base class: ABOVE")
    
    def is_below(self, subject, agent) :
        raise NotImplementedError("Error not implemented in base class: BELOW")
    
    def is_left_of(self, subject, agent):
        raise NotImplementedError("Error not implemented in base class: LEFT")

    def is_right_of(self, subject, agent):
        raise NotImplementedError("Error not implemented in base class: RIGHT")
    
    def _get_rectangle(self, body):
        raise NotImplementedError("Error not implemented in base class: BODY")
    
    
    
