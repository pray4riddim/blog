"""
首先将运算式从中缀转换成后缀式

再计算后缀表达式

"""
import re




def infix_to_postfix(expression):
    # 定义运算符优先级
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # 初始化堆栈和后缀表达式列表
    stack = []
    postfix = []

    # 将表达式字符串拆分为数字、运算符和括号
    tokens = re.findall(r'\d+(?:\.\d+)?|\S', expression)

    # 遍历中缀表达式的 tokens
    for token in tokens:
        # 如果是操作数，直接添加到后缀表达式列表
        if re.match(r'\d+(?:\.\d+)?', token):
            postfix.append(token)
        # 如果是'('，入栈
        elif token == '(':
            stack.append(token)
        
        elif token == ')':# 如果是')'，将栈中所有运算符弹出，并添加到后缀表达式列表
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # 弹出'('
        
        else:# 如果是运算符，弹出栈中所有优先级大于或等于当前运算符的运算符，并添加到后缀表达式列表
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(token)
            
    while stack:# 将栈中剩余的运算符添加到后缀表达式列表
        postfix.append(stack.pop())
        
    return ' '.join(postfix)# 返回后缀表达式字符串


#用于计算后缀表达式的函数
def evaluate_postfix(postfix_expression):
    stack = []
    tokens = postfix_expression.split()# 将后缀表达式字符串拆分为数字和运算符
    # 遍历后缀表达式的 tokens
    for token in tokens:
        # 如果是操作数，将其入栈
        if token.isnumeric():
            stack.append(float(token))
        # 如果是运算符，从栈中弹出两个操作数并进行计算，然后将结果入栈
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)
    return stack[-1]# 返回栈顶元素，即为计算结果


# 执行的运算操作
def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '^':
        return operand1 ** operand2
    else:
        raise ValueError("Invalid operator")


#运行计算器 在图形界面接口调用此函数
def main():
    a=input("enter the equation:")

    output = infix_to_postfix(a)
    
    print(output)

    return (evaluate_postfix(output))