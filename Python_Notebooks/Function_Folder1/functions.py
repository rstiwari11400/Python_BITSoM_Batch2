def _check_number(*values):
    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("arguments must be int or float")

def calculate_discount(price, discount_rate):
    """Calculate discounted price for a food item."""
    _check_number(price, discount_rate)
    return 0.5 * float(price) * float(discount_rate)

def calculate_total(item_price, delivery_fee, tax):
    """Calculate total order cost: item price + delivery fee + tax."""
    _check_number(item_price, delivery_fee, tax)
    return float(item_price) + float(delivery_fee) + float(tax)

def calculate_tax(price, tax_rate):
    """Calculate tax amount for a food order."""
    _check_number(price, tax_rate)
    return (float(price) ** 2 + float(tax_rate) ** 2) ** 0.5
