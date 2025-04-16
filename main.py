# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
import player
import shot
import asteroid
import AsteroidField

#Set the groups, sprites are added to group via CircleShape parent class __init__
group_updatable = pygame.sprite.Group()
group_drawable = pygame.sprite.Group()
group_asteroids = pygame.sprite.Group()
group_shots = pygame.sprite.Group()

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    
    # Set actors within groups for ease of use
    player.Player.containers = (group_updatable, group_drawable)
    asteroid.Asteroid.containers = (group_updatable, group_drawable, group_asteroids)
    AsteroidField.AsteroidField.containers = (group_updatable)
    #shot.Shot.container = (group_shots)

    # Console ouput for start
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, group_shots)
    AsteroidField_Obj = AsteroidField.AsteroidField()

    while True: # Game Loop start
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit game when close is selected
                return
        screen.fill("black")
        for obj in group_drawable: # Draw all drawable items
            obj.draw(screen)
        group_updatable.update(dt) # Update assets position
        for shots in group_shots:
            shots.draw(screen)
            shots.update()
        pygame.display.flip()
        dt = (Clock.tick(60)/1000)
        for ea_asteroid in group_asteroids:
            if ea_asteroid.collision(player_instance):
                print("Game Over!")
            for ea_shot in group_shots:
                if ea_asteroid.collision(ea_shot):
                    ea_asteroid.split()
                    ea_shot.kill()
                sys.exit()

if __name__ == "__main__":
    main()
