from turtle import width
import pyray
from services.physics_service import PhysicsService

class RaylibPhysicsService(PhysicsService) :
    def __init__(self) -> None:
        super().__init__()
    
    def subject_rectangle(self, subject):
        subject_rectangle = self._get_rectangle(subject)
        return subject_rectangle
    
    def agent_rectangle(self, agent):
        agent_rectangle = self._get_rectangle(agent)
        return agent_rectangle
    
    def collision_rectangle(self, subject, agent):
        subject_rectangle = self.subject_rectangle(subject)
        agent_rectangle = self.agent_rectangle(agent)
        return pyray.get_collision_rec(subject_rectangle, agent_rectangle)

    def has_collided(self, subject, agent) -> bool:
        subject_rectangle = self.subject_rectangle(subject)
        agent_rectangle = self.agent_rectangle(agent)
        return pyray.check_collision_recs(subject_rectangle, agent_rectangle)
    
    def is_above(self, subject, agent):
        subject_rectangle = self.subject_rectangle(subject)
        collision_rectangle = self.collision_rectangle(subject, agent)
        subject_rectangle_bottom = subject_rectangle.y + subject_rectangle.height
        collision_rectangle_bottom = collision_rectangle.y + collision_rectangle.height
        return subject_rectangle_bottom == collision_rectangle_bottom
    
    def is_left_of(self, subject, agent) :
        subject_rectangle = self.subject_rectangle(subject)
        collision_rectangle = self.collision_rectangle(subject, agent)
        subject_rectangle_right = subject_rectangle.x + subject_rectangle.width
        collision_rectangle_right = collision_rectangle.x + collision_rectangle.width
        return subject_rectangle_right == collision_rectangle_right
    
    def is_right_of(self, subject, agent) :
        subject_rectangle = self.subject_rectangle(subject)
        collision_rectangle = self.collision_rectangle(subject, agent)
        subject_rectangle_left = subject_rectangle.x
        collision_rectangle_left = collision_rectangle.x
        return subject_rectangle_left == collision_rectangle_left

    def _get_rectangle(self, body):
        top = body.get_position().get_y()
        left = body.get_position().get_x()
        width = body.get_position().get_x()
        height = body.get_size().get_y()
        return pyray.Rectangle(left, top, width, height)