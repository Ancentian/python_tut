weight = int(input("Weight in Kgs or L(bs): "))
unit = input("L or K ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"The weight is {converted} pounds")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} Kilos")