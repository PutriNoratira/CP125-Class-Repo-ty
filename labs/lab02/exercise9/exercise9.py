def calculate_xp_required(current_level):
    """
    Calculate XP needed for next level (level * 100).
    """
    return current_level * 100

def can_level_up(current_xp, required_xp):
    """
    Check if player has enough XP to level up.
    """
    return current_xp >= required_xp

def calculate_final_level(total_xp):
    """
    Calculate the final level reached.
    """
    level = 1
    while total_xp >= level * 100:
        total_xp = total_xp - (level * 100)
        level += 1
    return level

def calculate_remaining_xp(total_xp):
    """
    Calculate XP leftover after leveling.
    """
    level = 1
    while total_xp >= level * 100:
        total_xp = total_xp - (level * 100)
        level += 1
    return total_xp