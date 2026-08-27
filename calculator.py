import ast
from calculator_utils import safe_calculate

print("=" * 55)
print("      SAFE ADVANCED CALCULATOR - VERSION 7")
print("=" * 55)

print("\nSupported Operations:")
print("- Addition:         34 + 45")
print("- Subtraction:      50 - 12")
print("- Multiplication:   8 * 9")
print("- Division:         100 / 4")
print("- Parentheses:      (10 + 5) * 2")
print("- Exponentiation:   2 ** 3")
print("- Sine:             sin(1)")
print("- Cosine:           cos(1)")
print("- Tangent:          tan(1)")
print("- Square Root:      sqrt(81)")
print("- Logarithm:        log(100)")

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

print("Thank you for using the calculator!")