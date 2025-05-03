import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player,Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    prev = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    pj = Player(x,y)
    
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    
    Shot.containers = (shots,updatable,drawable)
        
    while True:
        # 3 pasos del GameLoop (https://gameprogrammingpatterns.com/game-loop.html)
        # Process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update game
        updatable.update(dt)
        
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collides(asteroid):
                    asteroid.split()
                    bullet.kill()
            
            if asteroid.collides(pj):
                print("Game over!")
                return
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        
        # Render
        pygame.display.flip()
        
        dt = prev.tick(60) / 1000
    

if __name__ == "__main__":
    main()