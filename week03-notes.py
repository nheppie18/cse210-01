"""
Class balloon:

color
max_volume
pop()
volume_ml

"""

import time

class Main:
    import Balloon
    def current_time_ms():
        return round(time.time() * 1000)
    
    print(current_time_ms())
    first_balloon = Balloon("Red")
    second_balloon = Balloon("Blue")
    balloon_list = []
    for i in range(10):
        balloon_list.append(Balloon("Green"))
    #While game is running
    first_balloon.update(current_time_ms())
    first_balloon.pop()
    
    for balloon in balloon_list:
        print(balloon)


class Balloon:
    def __init__(self, color):
        self.popped = False
        self.sealed = None
        self.volume_ml = None
        self.max_volume_ml = None
        self.update_time_ms = None
        self.color = color

    def pop(self):
        self.popped = True
        self.volume_ml = 0

    def decrease_air(self, delta_ms):
        pass

    def __str__(self) -> str:
        if self.popped:
            return "A big mess of elastic shards."
        return self.color + ": " + str(self.volume_ml)

    def update(time_ms, self):
        delta_ms = time_ms - self.update_time_ms
        
        # Update the air if it's not sealed
        if self.popped:
            self.volume_ml = 0
        elif self.sealed and self.volume_ml > 0:
            self.decrease_air(delta_ms)
        elif self.volume_ml > self.volume_max_ml:
            self.pop()
        
        self.update_time_ms = time_ms

