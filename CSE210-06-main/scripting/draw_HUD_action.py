from os import stat
from constants import *
from scripting.action import Action

class DrawHudAction(Action):
    
    def __init__(self, video_service) -> None:
        self._video_service = video_service
    
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_level(cast, LEVEL_GROUP, LEVEL_FORMAT, stats.get_level())
        self._draw_level(cast, LIVES_GROUP, LIVES_GROUP, stats.get_lives())
        self._draw_level(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())
    
    def _draw_level(self, cast, group, format_str, data):
        display_value = format_str.format(data)
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(display_value)
        position = label.get_position()
        self._video_service.draw_text(text, position)