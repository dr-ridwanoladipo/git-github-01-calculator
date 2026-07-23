import ast
import operator

print("=" * 55)
print("      SAFE ADVANCED CALCULATOR - VERSION 5")
print("=" * 55)

print("\nExamples:")
print("34 + 45")
print("34 + 45 * 87 - 89")
print("(10 + 5) * 2")
print("100 / 4 + 20")
print("2 ** 3")

allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def safe_calculate(node):
    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):
        left = safe_calculate(node.left)
        right = safe_calculate(node.right)
        operation = allowed_operators[type(node.op)]
        return operation(left, right)

    elif isinstance(node, ast.UnaryOp):
        value = safe_calculate(node.operand)
        operation = allowed_operators[type(node.op)]
        return operation(value)

    else:
        raise ValueError("Invalid or unsafe expression")


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
    print("\nError!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")