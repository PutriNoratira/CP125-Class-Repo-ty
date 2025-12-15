def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    """
    Checks if two rectangles are colliding (overlapping).
    
    Parameters:
    x1, y1: Top-left coordinate of Rectangle 1
    w1, h1: Width and Height of Rectangle 1
    x2, y2: Top-left coordinate of Rectangle 2
    w2, h2: Width and Height of Rectangle 2
    
    Returns:
    True if rectangles overlap, False otherwise
    
    Hint: It's easier to check when they DON'T overlap:
    - Rect 1 is completely to the left of Rect 2
    - Rect 1 is completely to the right of Rect 2
    - Rect 1 is completely above Rect 2
    - Rect 1 is completely below Rect 2
    
    If none of these are true, they must be overlapping!
    """
    # TODO: Implement collision detection logic
    no_overlap_x_left = (x1 + w1 <= x2)
    no_overlap_x_right = (x1 >= x2 + w2)
    no_overlap_y_above = (y1 + h1 <= y2)
    no_overlap_y_below = (y1 >= y2 + h2)

    if_not_overlap = (no_overlap_x_left or no_overlap_x_right or no_overlap_y_above or no_overlap_y_below)
    
    return not if_not_overlap