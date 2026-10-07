"""
Air Hockey (Lab Starter)
Run with:  python3 main.py
Controls: Arrow keys move your paddle (left side, blue).
"""

import pygame

from game.game_engine import GameEngine
from game.renderer import WINDOW_SIZE

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Air Hockey")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 24)

    engine = GameEngine()
    running = True
    while running:
        # Capture delta time (dt) in seconds and enforce 60 FPS
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        engine.handle_input(keys)
        
        # Pass dt to the engine for timer calculations
        engine.update(dt)
        
        engine.draw(screen, font)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
