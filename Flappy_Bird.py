import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

WHITE = (255, 255, 255)
BLUE = (0, 155, 255)
GREEN = (0, 200, 0)

clock = pygame.time.Clock()
FPS = 60

bird_size = 30
bird_x = 50
bird_y = HEIGHT // 2
bird_vel = 0
gravity = 0.4
flap_power = -7

pipe_width = 60
pipe_gap = 180
pipe_vel = 3
pipes = []  # list of (rect, pipe_id)

font = pygame.font.SysFont(None, 40)

score = 0
passed_pipes = set()
pipe_id_counter = 0

def draw_bird(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, bird_size, bird_size))

def create_pipe():
    global pipe_id_counter
    height = random.randint(100, 350)
    pipe_id_counter += 1
    pid = pipe_id_counter
    top_pipe = (pygame.Rect(WIDTH, 0, pipe_width, height), pid)
    bottom_pipe = (pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap), pid)
    return [top_pipe, bottom_pipe]

def move_pipes(pipes):
    new_pipes = []
    for rect, pid in pipes:
        rect.x -= pipe_vel
        if rect.x + pipe_width > 0:
            new_pipes.append((rect, pid))
    return new_pipes

def draw_pipes(pipes):
    for rect, pid in pipes:
        pygame.draw.rect(screen, GREEN, rect)

def check_collision(bird_rect, pipes):
    for rect, pid in pipes:
        if bird_rect.colliderect(rect):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return True
    return False

# First pipes
pipes.extend(create_pipe())

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = flap_power

    # Bird movement
    bird_vel += gravity
    bird_y += bird_vel

    # Move pipes
    pipes = move_pipes(pipes)

    # Add new pipes
    last_pipe_x = max([rect.x for rect, pid in pipes]) if pipes else 0
    if last_pipe_x < WIDTH - 200:
        pipes.extend(create_pipe())

    # Score update
    for rect, pid in pipes:
        if rect.x + pipe_width < bird_x and pid not in passed_pipes:
            score += 1
            passed_pipes.add(pid)

    # Draw elements
    draw_bird(bird_x, bird_y)
    draw_pipes(pipes)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Collision check
    bird_rect = pygame.Rect(bird_x, bird_y, bird_size, bird_size)
    if check_collision(bird_rect, pipes):
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

pygame.quit()
