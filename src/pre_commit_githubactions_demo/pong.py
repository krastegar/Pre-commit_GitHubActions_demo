import pygame


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, up, down, speed, height):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= speed
        if keys[down] and self.rect.bottom < height:
            self.rect.y += speed

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.dx, self.dy = 4, 4

    def move(self, width, height, left_paddle, right_paddle):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.dy *= -1

        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(
            right_paddle.rect
        ):
            self.dx *= -1

    def reset(self, x, y):
        self.rect.x, self.rect.y = x, y
        self.dx, self.dy = 4, 4

    def draw(self, screen, color):
        pygame.draw.ellipse(screen, color, self.rect)


class PongGame:
    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PADDLE_SPEED = 6

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.font = pygame.font.Font(None, 36)

        self.left_paddle = Paddle(20, self.HEIGHT // 2 - 50)
        self.right_paddle = Paddle(self.WIDTH - 30, self.HEIGHT // 2 - 50)
        self.ball = Ball(self.WIDTH // 2, self.HEIGHT // 2)

        self.left_score, self.right_score = 0, 0

    def run(self):
        running = True
        while running:
            pygame.time.delay(16)
            self.screen.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.left_paddle.move(
                pygame.K_w, pygame.K_s, self.PADDLE_SPEED, self.HEIGHT
            )
            self.right_paddle.move(
                pygame.K_UP, pygame.K_DOWN, self.PADDLE_SPEED, self.HEIGHT
            )
            self.ball.move(self.WIDTH, self.HEIGHT, self.left_paddle, self.right_paddle)

            if self.ball.rect.left <= 0:
                self.right_score += 1
                self.ball.reset(self.WIDTH // 2, self.HEIGHT // 2)
            if self.ball.rect.right >= self.WIDTH:
                self.left_score += 1
                self.ball.reset(self.WIDTH // 2, self.HEIGHT // 2)

            self.left_paddle.draw(self.screen, self.WHITE)
            self.right_paddle.draw(self.screen, self.WHITE)
            self.ball.draw(self.screen, self.WHITE)
            pygame.draw.aaline(
                self.screen,
                self.WHITE,
                (self.WIDTH // 2, 0),
                (self.WIDTH // 2, self.HEIGHT),
            )

            left_text = self.font.render(str(self.left_score), True, self.WHITE)
            right_text = self.font.render(str(self.right_score), True, self.WHITE)
            self.screen.blit(left_text, (self.WIDTH // 4, 20))
            self.screen.blit(right_text, (self.WIDTH * 3 // 4, 20))

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    PongGame().run()
