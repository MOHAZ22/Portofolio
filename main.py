import pygame
import sys
import random

# Initialize pygame
pygame.init()
try:
    pygame.mixer.init()
    move_sound = None
    gameover_sound = None
except pygame.error:
    move_sound = None
    gameover_sound = None

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

def random_position():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return x, y

def main():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = RIGHT
    food = random_position()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                    if move_sound: move_sound.play()
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                    if move_sound: move_sound.play()
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                    if move_sound: move_sound.play()
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                    if move_sound: move_sound.play()

        # Move snake
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0] * CELL_SIZE, head_y + direction[1] * CELL_SIZE)

        # Check collisions
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            if gameover_sound: gameover_sound.play()
            break  # Game over

        snake.insert(0, new_head)

        # Check food collision
        if new_head == food:
            score += 1
            food = random_position()
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(15)

    # Game over screen
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 48)
    game_over_text = font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 60))

    score_font = pygame.font.SysFont(None, 36)
    final_score_text = score_font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))

    info_text = score_font.render("Press R or Enter to Restart, Q to Quit", True, WHITE)
    screen.blit(info_text, (WIDTH // 2 - 170, HEIGHT // 2 + 40))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r or event.key == pygame.K_RETURN:
                    waiting = False
                    main()
        clock.tick(10)

if __name__ == "__main__":
    main()
