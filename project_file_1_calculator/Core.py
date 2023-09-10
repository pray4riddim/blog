import re


def is_number(token):
    try:
        # Check if the token is an integer or contains a decimal or negative sign
        int(token)
        return True
    except ValueError:
        if "." in token or "-" in token[1:]:
            return True
        else:
            return False


def infix_to_postfix(expression):
    operator_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = []
    postfix = ""
    tokens = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+|\*|\/|\+|\-|\(|\)", expression)

    for token in tokens:
        if is_number(token):
            postfix += token
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix += " " + stack.pop()
            stack.pop()
        else:
            while (
                stack
                and stack[-1] != "("
                and operator_precedence[token] <= operator_precedence.get(stack[-1], 0)
            ):
                postfix += " " + stack.pop()
            stack.append(token)

    while stack:
        postfix += " " + stack.pop()

    return postfix.strip()


def calculate_postfix_expression(expression):
    stack = []

    for char in expression:
        if char.isdigit() or char == ".":
            stack.append(float(char))
        elif char in ["+", "-", "*", "/"]:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 / operand2

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack[0]


def calculate(expression):
    return calculate_postfix_expression(infix_to_postfix(expression))
