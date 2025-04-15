import pygame
import sys
from game_engine import GameEngine

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Enchanted Forest")
    clock = pygame.time.Clock()
    
    game_engine = GameEngine(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
        
        game_engine.update()
        game_engine.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
