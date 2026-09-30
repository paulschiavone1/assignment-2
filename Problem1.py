# Problem 1: Customer Discount Eligibility

purchase = float(input("Enter purchase amount: $"))
member = input("Are you a member? (yes/no): ").strip().lower()

if member == "yes":
    if purchase >= 100:
        discount = 15
    else:
        discount = 5
else:
    if purchase >= 150:
        discount = 10
    else:
        discount = 0

final_price = purchase - (purchase * discount / 100)

print(f"Discount applied: {discount}%")
print(f"Final price: ${final_price:.2f}")