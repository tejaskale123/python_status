weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (k/l): ").lower()

if unit == "k":
    weight = weight * 2.205
    print(f"Your weight in pounds is: {weight:.2f} lbs")
elif unit == "l":
    weight = weight / 2.205
    print(f"Your weight in kilograms is: {weight:.2f} kg")
else:
    print(f"'{unit}' was not a valid unit.")
