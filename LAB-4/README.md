# LAB-4: Vibe Coding - Air Hockey (Pygame)

**SRN:** PES1UG24CS551
**Name:** Abhay Dubey H

An LLM-assisted (Google Gemini) fix and extension of a Pygame Air Hockey game. One deliberate bug was fixed and three features were added, each as a separate task and commit.

- **Repo link:** https://github.com/SETAPESU26/02_air_hockey
- **Chat history:** [PROMPTS-VIBE-CODING.pdf](PROMPTS-VIBE-CODING.pdf)
- **Chat link:** https://gemini.google.com/app/74d9dcbf646ed8af
- **Before video:** [Run_main_Before.mp4](Run_main_Before.mp4)
- **After video:** [Run_main_After.mp4](Run_main_After.mp4)
- **Summary:** [LAB4_SUMMARY.txt](LAB4_SUMMARY.txt)

---

## How to Run

Requires Python 3.10+.

```bash
cd LAB-4/air-hockey
pip install -r requirements.txt
python main.py
```

**Controls**

| Key | Action |
|-----|--------|
| Arrow keys | Move the blue paddle (left half of the table) |
| R | Restart the match (works at any time in the original; after game over in the AI-generated code) |

> Note: the AI-generated `handle_input` only checks the R key once `game_over` is True. If you need R to restart mid-match as the original README describes, move the R check above the `game_over` branch.

---

## Folder Structure

```
LAB-4/
├── air-hockey/
│   ├── main.py
│   ├── requirements.txt
│   └── game/
│       ├── game_engine.py
│       ├── puck.py
│       ├── paddle.py
│       ├── collisions.py
│       ├── ai.py
│       └── renderer.py
├── Run_main_Before.mp4
├── Run_main_After.mp4
├── PROMPTS-VIBE-CODING.pdf
├── LAB4_SUMMARY.txt
└── README.md
```

---

## What Was Done

### Task 1: Fix puck-paddle collision
**File:** `game/collisions.py`

**Bug:** the original handler only did `puck.vx = -puck.vx` when the circles overlapped. It ignored the impact angle and never moved the puck out of the paddle, so the puck could tunnel through or stay stuck inside.

**Fix:**
1. Compute the collision normal `(nx, ny)` from the paddle centre to the puck centre.
2. **Overlap resolution:** move the puck out by `(paddle.radius + puck.radius) - distance` along the normal.
3. **Reflection:** `v' = v - 2(v·n)n`, applied only if `v·n < 0` (puck moving into the paddle).
4. Handle `distance == 0` to avoid division by zero.

### Task 2: Match scoring
**Files:** `game/game_engine.py`, `game/renderer.py`

- New state: `player_score`, `computer_score`, `game_over`, `winner_text`.
- A goal counts only when the puck is within the goal gap (`GOAL_TOP < y < GOAL_BOTTOM`); otherwise it bounces off the end wall.
- `renderer.draw_hud()` shows both scores; `renderer.draw_game_over()` shows a dimmed overlay with the result.
- Game logic and player input freeze when `game_over` is True; **R** starts a new match.

### Task 3: 30-second match timer
**Files:** `main.py`, `game/game_engine.py`, `game/renderer.py`

- `main.py` computes `dt = clock.tick(60) / 1000.0` and calls `engine.update(dt)`, so timing is independent of frame rate.
- `time_left` counts down from `MATCH_TIME_SECONDS = 30.0` only while the match is active.
- At zero, `_end_match_by_time()` sets `game_over` and picks **Player Wins**, **Computer Wins**, or **Match Draw** from the scores.
- The remaining time is drawn at the top centre; **R** resets it to 30 s.

### Task 4: Puck reset after scoring
**Files:** `game/puck.py`, `game/paddle.py`, `game/game_engine.py`

- `Puck.reset(x, y)` places the puck at the centre and zeroes `vx`, `vy`.
- `Paddle` remembers `start_x` / `start_y`; `Paddle.reset()` returns it there.
- `GameEngine._reset_board(serve_direction)` resets the puck and both paddles, then calls `_launch_puck(serve_direction)` so the puck always continues play and is served towards the side that conceded.

---

## Prompting Strategy

One prompt per task, each with a role, numbered requirements, the current code, and the desired output format and design constraints (e.g. keep rendering in `renderer.py`, use `dt`). Each prompt included the latest code so changes built on each other. A short follow-up question caught an incomplete `renderer.py` snippet and produced the full merged file.

---

## Known Limitations

- The AI added an early win at `WINNING_SCORE = 5` alongside the timer. For a strict 30-second match as described in the task, raise `WINNING_SCORE` or remove the early finish in `_check_win_condition`.
- Paddle velocity is not added to the puck on impact.

---

## Git Workflow

Separate commits were made per task, for example:

```bash
git add game/collisions.py && git commit -m "Task 1: fix puck-paddle collision"
git add game/game_engine.py game/renderer.py && git commit -m "Task 2: add match scoring"
git add main.py game/game_engine.py game/renderer.py && git commit -m "Task 3: add 30-second timer"
git add game/puck.py game/paddle.py game/game_engine.py && git commit -m "Task 4: reset puck and paddles after goal"
```
