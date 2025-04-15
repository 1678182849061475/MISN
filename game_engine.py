import pygame

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (0, 128, 0)  # Green background
        self.player = pygame.Rect(375, 275, 50, 50)

    def update(self):
        keys = self.handle_input()
        if keys[pygame.K_LEFT]:
            self.player.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.x += 5
        if keys[pygame.K_UP]:
            self.player.y -= 5
        if keys[pygame.K_DOWN]:
            self.player.y += 5

    def draw(self):
        self.screen.fill(self.background_color)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        return keys
