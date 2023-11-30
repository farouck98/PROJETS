
def compute_discounted_price(original_price: float, discount_percentage: float):
         return original_price - (original_price * discount_percentage/100)
print(compute_discounted_price(100, 30))
