import unittest
import pygame
from src.pre_commit_githubactions_demo.pong import Ball, Paddle


class TestBall(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.ball = Ball(100, 100)
        self.screen = pygame.display.set_mode((800, 600))

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(self.ball.rect.x, 100)
        self.assertEqual(self.ball.rect.y, 100)
        self.assertEqual(self.ball.dx, 4)
        self.assertEqual(self.ball.dy, 4)

    def test_reset(self):
        self.ball.reset(200, 200)
        self.assertEqual(self.ball.rect.x, 200)
        self.assertEqual(self.ball.rect.y, 200)
        self.assertEqual(self.ball.dx, 4)
        self.assertEqual(self.ball.dy, 4)

    def test_draw(self):
        self.ball.draw(self.screen, (255, 255, 255))
        # No assertion, just ensuring no exceptions are raised


class TestPaddle(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.paddle = Paddle(100, 100)
        self.screen = pygame.display.set_mode((800, 600))

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(self.paddle.rect.x, 100)
        self.assertEqual(self.paddle.rect.y, 100)

    def test_draw(self):
        self.paddle.draw(self.screen, (255, 255, 255))
        # No assertion, just ensuring no exceptions are raised


if __name__ == "__main__":
    unittest.main()
