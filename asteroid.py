from circleshape import *
import random
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid1.velocity = pygame.Vector2(self.position.x, self.position.y).rotate(random.uniform(20, 50))
        asteroid1.velocity *= 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)        
        asteroid2.velocity = pygame.Vector2(self.position.x, self.position.y).rotate(-random.uniform(20, 50))
        asteroid2.velocity *= 1.2                      