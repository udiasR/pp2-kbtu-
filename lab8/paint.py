import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint - Extended")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [BLACK, RED, GREEN, BLUE]

# Default settings
default_size = 50
selected_color = BLACK
selected_shape = "rectangle"
fill_mode = False  # False for outlined, True for filled

def clear_screen():
    screen.fill(WHITE)
    pygame.display.update()

def draw_rectangle(x, y, width, height, color, fill):
    pygame.draw.rect(screen, color, (x, y, width, height), 0 if fill else 2)

def draw_circle(x, y, radius, color, fill):
    pygame.draw.circle(screen, color, (x, y), radius, 0 if fill else 2)

def draw_square(x, y, size, color, fill):
    pygame.draw.rect(screen, color, (x, y, size, size), 0 if fill else 2)

def draw_right_triangle(x, y, size, color, fill):
    points = [(x, y), (x, y + size), (x + size, y + size)]
    pygame.draw.polygon(screen, color, points, 0 if fill else 2)

def draw_equilateral_triangle(x, y, size, color, fill):
    height = (size * (3 ** 0.5)) / 2  # Height using 60-degree formula
    points = [(x, y + height), (x + size / 2, y), (x + size, y + height)]
    pygame.draw.polygon(screen, color, points, 0 if fill else 2)

def draw_rhombus(x, y, width, height, color, fill):
    points = [(x, y + height // 2), (x + width // 2, y), (x + width, y + height // 2), (x + width // 2, y + height)]
    pygame.draw.polygon(screen, color, points, 0 if fill else 2)

def erase(x, y, size):
    pygame.draw.rect(screen, WHITE, (x, y, size, size))

def change_color(index):
    global selected_color
    selected_color = COLORS[index % len(COLORS)]

def toggle_fill():
    global fill_mode
    fill_mode = not fill_mode

clear_screen()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_shape = "rectangle"
            elif event.key == pygame.K_2:
                selected_shape = "circle"
            elif event.key == pygame.K_3:
                selected_shape = "square"
            elif event.key == pygame.K_4:
                selected_shape = "right_triangle"
            elif event.key == pygame.K_5:
                selected_shape = "equilateral_triangle"
            elif event.key == pygame.K_6:
                selected_shape = "rhombus"
            elif event.key == pygame.K_e:
                selected_shape = "eraser"
            elif event.key == pygame.K_c:
                clear_screen()
            elif event.key == pygame.K_f:
                toggle_fill()
            elif event.key in [pygame.K_r, pygame.K_g, pygame.K_b, pygame.K_k]:
                if event.key == pygame.K_r:
                    selected_color = RED
                elif event.key == pygame.K_g:
                    selected_color = GREEN
                elif event.key == pygame.K_b:
                    selected_color = BLUE
                elif event.key == pygame.K_k:
                    selected_color = BLACK
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if selected_shape == "rectangle":
                draw_rectangle(x, y, default_size, default_size * 1.5, selected_color, fill_mode)
            elif selected_shape == "circle":
                draw_circle(x, y, default_size // 2, selected_color, fill_mode)
            elif selected_shape == "square":
                draw_square(x, y, default_size, selected_color, fill_mode)
            elif selected_shape == "right_triangle":
                draw_right_triangle(x, y, default_size, selected_color, fill_mode)
            elif selected_shape == "equilateral_triangle":
                draw_equilateral_triangle(x, y, default_size, selected_color, fill_mode)
            elif selected_shape == "rhombus":
                draw_rhombus(x, y, default_size, default_size, selected_color, fill_mode)
            elif selected_shape == "eraser":
                erase(x, y, default_size)
            pygame.display.update()

pygame.quit()
sys.exit()
