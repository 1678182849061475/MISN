import unittest
from game_engine import GameEngine
import pygame

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.game = GameEngine(self.screen)

    def test_player_initial_position(self):
        self.assertEqual(self.game.player.topleft, (375, 275))

    def tearDown(self):
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
