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
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
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


def calculate_bmi(weight, height):
    """Calculate BMI and return its health assessment."""
    if weight <= 0 or height <= 0:
        raise ValueError

    bmi = round(weight / height**2, 1)

    if bmi < 18.5:
        assessment = (
            "Underweight",
            "Below 18.5",
            "Your BMI is below the generally recommended healthy adult range "
            "(18.5-24.9).",
            "Aim for balanced, nutrient-rich meals containing adequate calories "
            "and protein. If your low weight is unintentional or associated with "
            "symptoms, consider speaking with a healthcare professional.",
        )

    elif bmi < 25:
        assessment = (
            "Normal Weight",
            "18.5-24.9",
            "Your BMI is within the generally recommended healthy adult range "
            "(18.5-24.9).",
            "Maintain your current weight with balanced meals, regular physical "
            "activity, adequate sleep and healthy lifestyle habits.",
        )

    elif bmi < 30:
        assessment = (
            "Overweight",
            "25.0-29.9",
            "Your BMI is above the generally recommended healthy adult range "
            "(18.5-24.9).",
            "Focus on balanced meals rich in vegetables, fruits, whole grains "
            "and lean protein. Reduce highly processed foods and sugary drinks, "
            "and maintain regular physical activity.",
        )

    elif bmi < 35:
        assessment = (
            "Obesity Class I",
            "30.0-34.9",
            "Your BMI is within the Obesity Class I range and is above the "
            "generally recommended healthy adult range (18.5-24.9).",
            "Consider gradual, sustainable weight management through balanced "
            "nutrition, regular physical activity and healthy daily habits. "
            "A healthcare professional can help assess additional health risks "
            "if needed.",
        )

    elif bmi < 40:
        assessment = (
            "Obesity Class II",
            "35.0-39.9",
            "Your BMI is within the Obesity Class II range and is well above "
            "the generally recommended healthy adult range (18.5-24.9).",
            "Consider discussing weight management and your overall health with "
            "a healthcare professional. Balanced nutrition, regular activity "
            "and sustainable lifestyle changes remain important.",
        )

    else:
        assessment = (
            "Obesity Class III",
            "40.0 or above",
            "Your BMI is within the Obesity Class III range and is substantially "
            "above the generally recommended healthy adult range (18.5-24.9).",
            "Consider speaking with a healthcare professional for a more "
            "complete health assessment and an individualized, safe "
            "weight-management plan.",
        )

    return bmi, assessment