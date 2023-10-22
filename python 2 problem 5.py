talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
talent_to_pound = 20
pound_to_lot = 32
lot_to_grams = 13.3

grams = (talents * talent_to_pound + pounds) * pound_to_lot * lot_to_grams
kilograms = grams / 1000

print(f"The mass is equivalent to {int(kilograms)} kilograms and {int(grams % 1000)} grams.")