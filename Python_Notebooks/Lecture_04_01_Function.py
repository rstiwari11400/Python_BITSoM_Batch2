from Function_Folder1.functions import calculate_discount, calculate_total, calculate_tax


discount = calculate_discount(12, 0.5)           # 50% discount on a $12 burger
total    = calculate_total(12, 5.99, 1.50)       # item + delivery fee + tax
tax      = calculate_tax(12, 1.50)               # tax calculation
tax      = calculate_tax(12, '1.50')             # intentional TypeError: must be numbers
print(f"Discount Amount : {discount}")
print(f"Order Total     : {total}")
print(f"Tax Amount      : {tax}")