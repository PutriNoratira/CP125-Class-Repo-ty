
def is_safe_time(hour, temperature):
    """
    Returns False if 10 <= hour <= 16 (10 AM to 4 PM),
    UNLESS temperature > 40.
    """
    if temperature > 40:
        return True
    
    if 10 <= hour <= 16:
        return False
    
    return True

def needs_moisture(moisture_level):
    """
    Returns True if moisture < 30.
    """
    return moisture_level < 30

def should_trigger_pump(moisture, hour, temp):
    """
    Returns True if it needs moisture AND is a safe time.
    """
    if moisture >= 30:
        return False
    
    if temp > 40:
        return True
    
    if 10 <= hour <= 16:
        return False
    
    return True