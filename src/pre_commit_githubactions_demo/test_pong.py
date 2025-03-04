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

    def test_move(self):
        left_paddle = Paddle(20, 250)
        right_paddle = Paddle(770, 250)
        self.ball.move(800, 600, left_paddle, right_paddle)
        self.assertEqual(self.ball.rect.x, 104)
        self.assertEqual(self.ball.rect.y, 104)

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

    def test_move(self):
        self.paddle.move(pygame.K_w, pygame.K_s, 6, 600)
        keys = pygame.key.get_pressed()
        keys[pygame.K_w] = True
        self.assertEqual(self.paddle.rect.y, 94)

    def test_draw(self):
        self.paddle.draw(self.screen, (255, 255, 255))
        # No assertion, just ensuring no exceptions are raised


if __name__ == "__main__":
    unittest.main()
