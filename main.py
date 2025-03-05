# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid) is True:
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.check_collision(asteroid) is True:
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60)/1000        

if __name__ == "__main__":
    main()