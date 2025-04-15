import unittest
import pygame
from utils import load_image

class TestUtils(unittest.TestCase):
    def test_load_image(self):
        image = load_image("https://via.placeholder.com/150")
        self.assertIsInstance(image, pygame.Surface)

if __name__ == "__main__":
    unittest.main()
