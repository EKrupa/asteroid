import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self,circleshape2):
        distance = pygame.math.Vector2.distance_to(self.position, circleshape2.position)
        if distance <= (self.radius + circleshape2.radius):
            return True
        else:
            return False
       