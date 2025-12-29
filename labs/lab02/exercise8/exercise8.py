def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    height = current_height * 0.8
    return height

def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    return height < 1

def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    count = 0
    current_height = initial_height

    while True:
        current_height = calculate_bounce_height(current_height)
        if is_ball_stopped(current_height):
            break
         
    

def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    