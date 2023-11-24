
def compute_discounted_price(op: float, dp: float):
         dp = float(dp/100)
         result = float(op) - (float(op) * dp)
         return result
print(compute_discounted_price(110, 30))
