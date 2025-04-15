import pygame

def load_image(url):
    image = pygame.image.load(url)
    return image.convert_alpha()

def handle_input():
    keys = pygame.key.get_pressed()
    return keys
