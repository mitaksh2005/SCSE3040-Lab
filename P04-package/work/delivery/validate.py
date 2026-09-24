"""Is this order usable?"""

def is_valid_order(order):
    """True if the order passes every rule."""
    if order.get("distance_km", 0) <= 0:
        return False
    if order.get("prep_time_min", -1) < 0:
        return False
    if order.get("traffic_level") not in (1, 2, 3):
        return False
    if order.get("rain") not in (0, 1):
        return False
    return True
