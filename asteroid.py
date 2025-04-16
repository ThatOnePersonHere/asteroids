from circleshape import *
from constants import *
import random

# Asteroid class, child from circleshape class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle( screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_speed = (random.randint(12, 16)/10)
        print(self.velocity)
        asteroid_1 = Asteroid(self.position.x+5, self.position.y-5, new_radius)
        asteroid_1.velocity = (pygame.Vector2(self.velocity).rotate(random_angle)*new_speed)
        asteroid_2 = Asteroid(self.position.x-5, self.position.y+5, new_radius)
        asteroid_2.velocity = (pygame.Vector2(self.velocity).rotate(-random_angle)*new_speed)