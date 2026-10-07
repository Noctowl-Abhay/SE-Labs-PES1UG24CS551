import math

def handle_paddle_collision(puck, paddle):
    """
    If the puck overlaps the paddle, resolve overlap and bounce it off
    using 2D circle-to-circle collision vector math.
    Returns True if a collision was handled this frame.
    """
    dx = puck.x - paddle.x
    dy = puck.y - paddle.y
    distance = math.hypot(dx, dy)
    
    min_dist = puck.radius + paddle.radius

    if distance < min_dist:
        # Prevent division by zero if centers perfectly overlap
        if distance == 0:
            nx, ny = 1, 0 
        else:
            # Calculate the collision normal (unit vector)
            nx = dx / distance
            ny = dy / distance

        # 1. Overlap Resolution (Position Correction)
        # Push the puck out along the normal so they no longer intersect
        overlap = min_dist - distance
        puck.x += nx * overlap
        puck.y += ny * overlap

        # 2. Velocity Reflection using Dot Product
        # Find how much of the puck's velocity is moving directly into the paddle
        dot_product = puck.vx * nx + puck.vy * ny

        # Only apply bounce if the puck is moving towards the paddle
        # (Prevents getting stuck if the paddle overtakes the puck from behind)
        if dot_product < 0:
            # Reflection formula: v_new = v - 2 * (v · n) * n
            puck.vx -= 2 * dot_product * nx
            puck.vy -= 2 * dot_product * ny
            
            # Note: If your paddle has a velocity (e.g., paddle.vx, paddle.vy), 
            # you can add paddle momentum to the puck here.

        return True

    return False
