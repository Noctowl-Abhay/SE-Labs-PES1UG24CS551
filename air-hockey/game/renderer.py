"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame

WIDTH, HEIGHT = 800, 500
MARGIN = 20
GOAL_HEIGHT = 150
GOAL_TOP = HEIGHT / 2 - GOAL_HEIGHT / 2
GOAL_BOTTOM = HEIGHT / 2 + GOAL_HEIGHT / 2

COLOR_BG = (15, 15, 25)
COLOR_TABLE = (20, 60, 90)
COLOR_WALL = (200, 200, 210)
COLOR_CENTER_LINE = (90, 130, 150)
COLOR_PUCK = (240, 240, 240)
COLOR_PLAYER = (60, 140, 240)
COLOR_COMPUTER = (240, 80, 80)
COLOR_TEXT = (255, 255, 255)

WINDOW_SIZE = (WIDTH, HEIGHT)


def draw_table(surface):
    surface.fill(COLOR_BG)
    pygame.draw.rect(surface, COLOR_TABLE, (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN))
    pygame.draw.line(surface, COLOR_CENTER_LINE, (WIDTH / 2, MARGIN), (WIDTH / 2, HEIGHT - MARGIN), 2)

    pygame.draw.rect(surface, COLOR_WALL, (0, 0, WIDTH, MARGIN))
    pygame.draw.rect(surface, COLOR_WALL, (0, HEIGHT - MARGIN, WIDTH, MARGIN))
    pygame.draw.rect(surface, COLOR_WALL, (0, MARGIN, MARGIN, GOAL_TOP - MARGIN))
    pygame.draw.rect(surface, COLOR_WALL, (0, GOAL_BOTTOM, MARGIN, HEIGHT - MARGIN - GOAL_BOTTOM))
    pygame.draw.rect(surface, COLOR_WALL, (WIDTH - MARGIN, MARGIN, MARGIN, GOAL_TOP - MARGIN))
    pygame.draw.rect(surface, COLOR_WALL, (WIDTH - MARGIN, GOAL_BOTTOM, MARGIN, HEIGHT - MARGIN - GOAL_BOTTOM))


def draw_puck(surface, puck):
    pygame.draw.circle(surface, COLOR_PUCK, (int(puck.x), int(puck.y)), puck.radius)


def draw_paddle(surface, paddle, color):
    pygame.draw.circle(surface, color, (int(paddle.x), int(paddle.y)), int(paddle.radius))


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_banner(surface, font, text):
    surf = font.render(text, True, (255, 220, 80))
    rect = surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
    surface.blit(surf, rect)
    
    import pygame

# Assuming existing constants are here: WIDTH, HEIGHT, COLOR_PLAYER, etc.
COLOR_TEXT = (255, 255, 255)
COLOR_OVERLAY = (0, 0, 0, 150) # Semi-transparent black

def draw_hud(surface, font, player_score, computer_score):
    """Draws the current score at the top center of the board."""
    # Player Score
    p_text = font.render(str(player_score), True, COLOR_TEXT)
    p_rect = p_text.get_rect(center=(WIDTH * 0.25, 40))
    surface.blit(p_text, p_rect)

    # Computer Score
    c_text = font.render(str(computer_score), True, COLOR_TEXT)
    c_rect = c_text.get_rect(center=(WIDTH * 0.75, 40))
    surface.blit(c_text, c_rect)

    # Center Divider / Hyphen
    div_text = font.render("-", True, COLOR_TEXT)
    div_rect = div_text.get_rect(center=(WIDTH / 2, 40))
    surface.blit(div_text, div_rect)

def draw_game_over(surface, font, winner_text):
    """Draws a darkened overlay and the winning message."""
    # Darken screen
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill(COLOR_OVERLAY)
    surface.blit(overlay, (0, 0))

    # Draw Game Over Text
    text_surf = font.render(winner_text, True, COLOR_TEXT)
    text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    surface.blit(text_surf, text_rect)
