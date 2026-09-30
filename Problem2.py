# Problem 2: Employee Performance Bonus

salary = float(input("Enter annual salary: $"))
score = int(input("Enter performance score: "))

if score >= 90:
    bonus_percent = 20
elif score >= 80:
    bonus_percent = 10
elif score >= 70:
    bonus_percent = 5
else:
    bonus_percent = 0

bonus = salary * bonus_percent / 100

print(f"Performance Bonus: {bonus_percent}%")
print(f"Bonus Amount: ${bonus:,.2f}")