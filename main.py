import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable,)
    field = AsteroidField()

   


    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   

    

    
    

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
        updateable.update(dt)
        for a in asteroids:
            if a.check_collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if a.check_collision(shot):
                    shot.kill()
                    a.split()

              
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 player.shoot()

        

       

   

    


if __name__ == "__main__":
    main()