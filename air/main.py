import time
from  air.balloon import Balloon
from clown import Clown
import random

class Main:
    def current_time_ms():
        return round(time.time() * 1000)
    
    clown = Clown()
    print(current_time_ms())
    first_balloon = clown.buy_balloon(3)
    second_balloon = clown.buy_balloon(3)
    balloon_list = []
    for i in range(10):
        balloon_list.append(clown.buy_balloon(random.randint(1,13)))
    #While game is running
    first_balloon.update(current_time_ms())
    first_balloon.pop()
    balloon_list[random.randint(0,len(balloon_list) - 1)].pop()
    for balloon in balloon_list:
        print(balloon)