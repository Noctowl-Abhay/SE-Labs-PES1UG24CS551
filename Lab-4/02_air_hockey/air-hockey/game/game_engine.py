"""
GameEngine: owns the puck, both paddles, and the computer AI, and runs
one frame's worth of game logic.
"""

import random
import pygame

from game.puck import Puck
from game.paddle import Paddle
from game.ai import ComputerAI
from game.collisions import handle_paddle_collision
from game.renderer import WIDTH, HEIGHT, MARGIN, GOAL_TOP, GOAL_BOTTOM

PLAYER_SPEED = 6
PUCK_RADIUS = 12
PADDLE_RADIUS = 28
INITIAL_PUCK_SPEED = 4.5
WINNING_SCORE = 5  
MATCH_TIME_SECONDS = 30.0


class GameEngine:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.game_over = False
        self.winner_text = ""
        self.time_left = MATCH_TIME_SECONDS

        self.player_start_pos = (WIDTH * 0.15, HEIGHT / 2)
        self.computer_start_pos = (WIDTH * 0.85, HEIGHT / 2)

        self.puck = Puck(WIDTH / 2, HEIGHT / 2, PUCK_RADIUS)
        
        self.player = Paddle(
            x=self.player_start_pos[0], y=self.player_start_pos[1], radius=PADDLE_RADIUS,
            min_x=MARGIN + PADDLE_RADIUS, max_x=WIDTH / 2 - PADDLE_RADIUS,
            min_y=MARGIN + PADDLE_RADIUS, max_y=HEIGHT - MARGIN - PADDLE_RADIUS,
        )
        self.computer = Paddle(
            x=self.computer_start_pos[0], y=self.computer_start_pos[1], radius=PADDLE_RADIUS,
            min_x=WIDTH / 2 + PADDLE_RADIUS, max_x=WIDTH - MARGIN - PADDLE_RADIUS,
            min_y=MARGIN + PADDLE_RADIUS, max_y=HEIGHT - MARGIN - PADDLE_RADIUS,
        )
        self.ai = ComputerAI()
        self._launch_puck()

    def _launch_puck(self, serve_direction=None):
        """Launches the puck. If serve_direction is specified, routes it toward that side."""
        angle_choices = [0.3, 0.6, -0.3, -0.6]
        
        # If no direction specified (e.g. game start), pick randomly
        if serve_direction is None:
            direction = random.choice([-1, 1])
        else:
            direction = serve_direction
            
        vy_factor = random.choice(angle_choices)
        self.puck.vx = INITIAL_PUCK_SPEED * direction
        self.puck.vy = INITIAL_PUCK_SPEED * vy_factor

    def _handle_goals(self):
        # Left goal (Computer scores)
        if self.puck.x - self.puck.radius < MARGIN:
            if GOAL_TOP < self.puck.y < GOAL_BOTTOM:
                self.computer_score += 1
                self._check_win_condition(serve_direction=-1)  # Serve to left (Player)
            else:
                self.puck.x = MARGIN + self.puck.radius
                self.puck.vx = -self.puck.vx
                
        # Right goal (Player scores)
        elif self.puck.x + self.puck.radius > WIDTH - MARGIN:
            if GOAL_TOP < self.puck.y < GOAL_BOTTOM:
                self.player_score += 1
                self._check_win_condition(serve_direction=1)  # Serve to right (Computer)
            else:
                self.puck.x = WIDTH - MARGIN - self.puck.radius
                self.puck.vx = -self.puck.vx

    def _check_win_condition(self, serve_direction=None):
        if self.player_score >= WINNING_SCORE:
            self.game_over = True
            self.winner_text = "Player Wins! Press 'R' to Restart"
        elif self.computer_score >= WINNING_SCORE:
            self.game_over = True
            self.winner_text = "Computer Wins! Press 'R' to Restart"
        else:
            self._reset_board(serve_direction)

    def _reset_board(self, serve_direction=None):
        """Cleans board state entirely using class-level resets."""
        # Reset puck to exact center and clear velocity
        self.puck.reset(WIDTH / 2, HEIGHT / 2)
        
        # Reset paddles to their starting halves, ensuring no overlap
        self.player.reset()
        self.computer.reset()
        
        # Launch the puck to the player who conceded
        self._launch_puck(serve_direction)

    def _reset_match(self):
        """Resets the entire game after a win."""
        self.player_score = 0
        self.computer_score = 0
        self.game_over = False
        self.winner_text = ""
        self.time_left = MATCH_TIME_SECONDS  
        self._reset_board(serve_direction=None)  # Random serve on entirely new match

    def handle_input(self, keys_pressed):
        if self.game_over:
            if keys_pressed[pygame.K_r]:
                self._reset_match()
            return  

        dx = dy = 0
        if keys_pressed[pygame.K_UP]:
            dy -= PLAYER_SPEED
        if keys_pressed[pygame.K_DOWN]:
            dy += PLAYER_SPEED
        if keys_pressed[pygame.K_LEFT]:
            dx -= PLAYER_SPEED
        if keys_pressed[pygame.K_RIGHT]:
            dx += PLAYER_SPEED
        self.player.move_by(dx, dy)

    def update(self, dt):
        if self.game_over:
            return 

        # Timer countdown logic
        self.time_left -= dt
        if self.time_left <= 0:
            self.time_left = 0
            self._end_match_by_time()
            return  # Skip physics updates for this frame

        self.ai.update(self.computer, self.puck)

        self.puck.move()
        self.puck.bounce_off_walls(HEIGHT, MARGIN)

        handle_paddle_collision(self.puck, self.player)
        handle_paddle_collision(self.puck, self.computer)

        self._handle_goals()

    def _end_match_by_time(self):
        """Triggered when the 30-second timer hits 0."""
        self.game_over = True
        if self.player_score > self.computer_score:
            self.winner_text = "Time Up! Player Wins! Press 'R' to Restart"
        elif self.computer_score > self.player_score:
            self.winner_text = "Time Up! Computer Wins! Press 'R' to Restart"
        else:
            self.winner_text = "Time Up! Match Draw! Press 'R' to Restart"

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_table(surface)
        renderer.draw_paddle(surface, self.player, renderer.COLOR_PLAYER)
        renderer.draw_paddle(surface, self.computer, renderer.COLOR_COMPUTER)
        renderer.draw_puck(surface, self.puck)
        
        # Pass time_left to the renderer
        renderer.draw_hud(surface, font, self.player_score, self.computer_score, self.time_left)
        if self.game_over:
            renderer.draw_game_over(surface, font, self.winner_text)
