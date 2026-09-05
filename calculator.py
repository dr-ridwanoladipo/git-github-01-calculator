import ast
import textwrap

from calculator_utils import calculate_bmi, safe_calculate


WIDTH = 55


def run_bmi_calculator():
    """Run the BMI calculator."""
    print("\n" + "=" * WIDTH)
    print("                 BMI CALCULATOR")
    print("=" * WIDTH)

    try:
        weight = float(input("\nEnter weight (kg): "))
        height = float(input("Enter height (m): "))

        bmi, assessment = calculate_bmi(weight, height)
        category, bmi_range, health_note, recommendation = assessment

        print("\nBMI RESULT")
        print("-" * WIDTH)
        print(f"Weight:        {weight:g} kg")
        print(f"Height:        {height:g} m")
        print(f"BMI:           {bmi}")
        print(f"Category:      {category}")
        print(f"BMI Range:     {bmi_range}")

        print("\nHealth note:")
        print(textwrap.fill(health_note, WIDTH))

        print("\nRecommendation:")
        print(textwrap.fill(recommendation, WIDTH))

        print("\nNote:")
        print(
            textwrap.fill(
                "BMI is a screening tool, not a diagnosis. Factors such as "
                "age, muscle mass, pregnancy and medical conditions may affect "
                "its interpretation.",
                WIDTH,
            )
        )

        print("=" * WIDTH)

        return f"BMI: {bmi} ({category}; {weight:g} kg, {height:g} m)"

    except ValueError:
        print("\nError: Weight and height must be valid positive numbers.")


print("=" * WIDTH)
print("      SAFE ADVANCED CALCULATOR - VERSION 9")
print("=" * WIDTH)

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

print("\nCommands:")
print("- history: Show previous calculations")
print("- bmi:     Calculate Body Mass Index")
print("- exit:    Close the calculator")

history = []

while True:
    expression = input("\nEnter your calculation or command: ").strip()

    if expression.lower() == "exit":
        break

    if expression.lower() == "history":
        if history:
            print("\nCalculation History:")

            for item in history:
                print(item)
        else:
            print("\nNo calculations yet.")

        continue

    if expression.lower() == "bmi":
        result = run_bmi_calculator()

        if result:
            history.append(result)

        continue

    if not expression:
        print("\nError: Please enter a calculation or command.")
        continue

    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_calculate(tree.body)

        calculation = f"{expression} = {result}"

        print("\n" + "=" * WIDTH)
        print("CALCULATION RESULT")
        print("=" * WIDTH)
        print(calculation)

        history.append(calculation)

    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")

    except Exception:
        print("\nError: Invalid or unsafe calculation entered.")

print("Thank you for using the calculator!")