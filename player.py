from circleshape import *
from constants import *
import shot
#from main import group_shots

class Player(CircleShape):
    def __init__(self,x,y, shot_group):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_group = shot_group
        self.timer = 0
    
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # Draw the triangle

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot_instance = shot.Shot(self.position.x, self.position.y)
            shot_instance.velocity = (pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED)
            self.shot_group.add(shot_instance)
            self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -=  dt

        if keys[pygame.K_a]: # Key a pressed to rotate left
            self.rotate(-dt)

        if keys[pygame.K_d]: # Key d pressed to rotate right
            self.rotate(dt)

        if keys[pygame.K_w]: # Key w pressed to move forward
            self.move(dt)

        if keys[pygame.K_s]: # Key s pressed to move backwards
            self.move(-dt)

        if keys[pygame.K_SPACE]: # Key spacebar to shoot
            self.shoot()