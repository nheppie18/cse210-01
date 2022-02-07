class Balloon:
    def __init__(self, color):
        self.popped = False
        self.sealed = False
        self.volume_ml = 0
        self.max_volume_ml = 1000
        self.update_time_ms = 0
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

    def fill(self, volume_ml):
        self.volume_ml += volume_ml
        if self.volume_ml > self.volume_max_ml:
            self.pop()
