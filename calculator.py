print("=" * 50)
print("      ADVANCED CALCULATOR - VERSION 4")
print("=" * 50)

print("\nExamples:")
print("34 + 45")
print("34 + 45 * 87 - 89")
print("(10 + 5) * 2")
print("100 / 4 + 20")

expression = input("\nEnter your calculation: ")

try:
    result = eval(expression)

    print("\n" + "=" * 50)
    print("CALCULATION")
    print("=" * 50)

    print(f"{expression} = {result}")

except Exception:
    print("\nError!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")