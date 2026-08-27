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
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
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
        if (
                not isinstance(node.func, ast.Name)
                or node.func.id not in allowed_functions
                or len(node.args) != 1
                or node.keywords
        ):
            raise ValueError("Invalid or unsupported function call")

        argument = safe_calculate(node.args[0])
        return allowed_functions[node.func.id](argument)

    raise ValueError("Invalid or unsafe expression")