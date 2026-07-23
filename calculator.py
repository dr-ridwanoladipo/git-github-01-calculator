import ast
from calculator_utils import safe_calculate

print("=" * 55)
print("      SAFE ADVANCED CALCULATOR - VERSION 5")
print("=" * 55)

print("\nExamples:")
print("34 + 45")
print("34 + 45 * 87 - 89")
print("(10 + 5) * 2")
print("100 / 4 + 20")
print("2 ** 3")

expression = input("\nEnter your calculation: ")

try:
    tree = ast.parse(expression, mode="eval")
    result = safe_calculate(tree.body)

    print("\n" + "=" * 55)
    print("SAFE CALCULATION")
    print("=" * 55)
    print(f"{expression} = {result}")

except ZeroDivisionError:
    print("\nError: Cannot divide by zero.")

except Exception:
    print("\nError: Invalid or unsafe calculation entered.")
