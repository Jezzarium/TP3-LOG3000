from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Map operator symbols to their corresponding functions
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Parses and evaluates a simple mathematical expression.

    Supported operators: +, -, *, /
    The expression should contain two numbers separated by an operator.

    Args:
        expr (str): The mathematical expression string (e.g., "5 + 3").

    Returns:
        float: The result of the calculation.

    Raises:
        ValueError: If the expression is invalid, empty, contains multiple operators,
                    or if operands are not valid numbers.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles requests to the root URL.

    GET: Renders the calculator interface.
    POST: Processes the calculation form submission.

    Returns:
        str: Rendered HTML template with the result (if any).
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)