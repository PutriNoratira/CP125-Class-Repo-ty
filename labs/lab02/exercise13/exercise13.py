
def get_rate_per_kg(destination):
    """
    Returns 5.0 for Domestic, 15.0 for International.
    """
    if destination == "International":
        return 15.00
    elif destination == "Domestic" :
        return 5.00
    
def get_express_charge(is_express):
    """
    Returns 10.0 if is_express is True, otherwise 0.0.
    """
    if is_express:
        return 10.00
    return 0.00
    
def calculate_shipping_quote(weight, destination, is_express):
    """
    Calculates final quote: (weight * rate) + express_charge
    """
    if destination == "International":
        rate = 15.00
    elif destination == "Domestic" :
        rate = 5.00

    total_cost = weight * rate

    if is_express:
        total_cost += 10.00

    return total_cost