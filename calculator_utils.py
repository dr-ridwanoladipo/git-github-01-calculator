import ast
import operator

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

    raise ValueError("Invalid or unsafe expression")