import ast
import math
import operator

allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

allowed_functions = {
    "sqrt": math.sqrt,
    "log": math.log10,
}

def safe_calculate(node):
    """Safely evaluate a supported arithmetic expression node."""
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

    elif isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function")

        function_name = node.func.id

        if function_name not in allowed_functions:
            raise ValueError("Unsupported function")

        arguments = [safe_calculate(arg) for arg in node.args]

        return allowed_functions[function_name](*arguments)

    raise ValueError("Invalid or unsafe expression")