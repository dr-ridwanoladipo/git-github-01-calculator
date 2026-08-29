import ast
from calculator_utils import safe_calculate

print("=" * 55)
print("      SAFE ADVANCED CALCULATOR - VERSION 8")
print("=" * 55)

print("\nSupported Operations:")
print("- Addition:         34 + 45")
print("- Subtraction:      50 - 12")
print("- Multiplication:   8 * 9")
print("- Division:         100 / 4")
print("- Parentheses:      (10 + 5) * 2")
print("- Exponentiation:   2 ** 3")
print("- Sine:             sin(30)")
print("- Cosine:           cos(60)")
print("- Tangent:          tan(45)")
print("- Square Root:      sqrt(81)")
print("- Logarithm:        log(100)")

history = []

while True:
    expression = input("\nEnter your calculation: ").strip()

    if not expression:
        print("\nError: Please enter a calculation.")
        continue

    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_calculate(tree.body)

        calculation = f"{expression} = {result}"

        print("\n" + "=" * 55)
        print("CALCULATION RESULT")
        print("=" * 55)
        print(calculation)

        history.append(calculation)

    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")

    except Exception:
        print("\nError: Invalid or unsafe calculation entered.")

print("Thank you for using the calculator!")