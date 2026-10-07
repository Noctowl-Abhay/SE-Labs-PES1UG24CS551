"""
GameEngine: owns the puck, both paddles, and the computer AI, and runs
one frame's worth of game logic.

Starter version: the puck bounces around and paddles can hit it, but
there is no scoring, no match timer, and the reset that happens after
a goal is incomplete. That's what Tasks 2-4 fix/add.
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
MATCH_TIME_SECONDS = 30.0  # Added match timer constant

class GameEngine:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.game_over = False
        self.winner_text = ""
        self.time_left = MATCH_TIME_SECONDS  # Initialize match time

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

    def _launch_puck(self):
        angle_choices = [0.3, 0.6, -0.3, -0.6]
        direction = random.choice([-1, 1])
        vy_factor = random.choice(angle_choices)
        self.puck.vx = INITIAL_PUCK_SPEED * direction
        self.puck.vy = INITIAL_PUCK_SPEED * vy_factor

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
            return # Skip physics updates for this frame

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

    def _handle_goals(self):
        if self.puck.x - self.puck.radius < MARGIN:
            if GOAL_TOP < self.puck.y < GOAL_BOTTOM:
                self.computer_score += 1
                self._check_win_condition()
            else:
                self.puck.x = MARGIN + self.puck.radius
                self.puck.vx = -self.puck.vx
                
        elif self.puck.x + self.puck.radius > WIDTH - MARGIN:
            if GOAL_TOP < self.puck.y < GOAL_BOTTOM:
                self.player_score += 1
                self._check_win_condition()
            else:
                self.puck.x = WIDTH - MARGIN - self.puck.radius
                self.puck.vx = -self.puck.vx

    def _check_win_condition(self):
        """Retained for early wins if a player reaches WINNING_SCORE before time is up."""
        if self.player_score >= WINNING_SCORE:
            self.game_over = True
            self.winner_text = "Player Wins! Press 'R' to Restart"
        elif self.computer_score >= WINNING_SCORE:
            self.game_over = True
            self.winner_text = "Computer Wins! Press 'R' to Restart"
        else:
            self._reset_board()

    def _reset_board(self):
        self.puck.x, self.puck.y = WIDTH / 2, HEIGHT / 2
        self._launch_puck()
        self.player.x, self.player.y = self.player_start_pos
        self.computer.x, self.computer.y = self.computer_start_pos

    def _reset_match(self):
        self.player_score = 0
        self.computer_score = 0
        self.game_over = False
        self.winner_text = ""
        self.time_left = MATCH_TIME_SECONDS  # Reset timer on match restart
        self._reset_board()

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
