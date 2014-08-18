from bei_functions import *
from bei_exceptions import *

keywords = ['true', 'false', 'and', 'or', 'not', '(', ')']

literals  = {'true': True, 'false': False}
operators = {'and': bei_and, 'or': bei_or, 'not': bei_not}
num_args  = {'and': 2, 'or': 2, 'not': 1}

# en.wikipedia.org/wiki/Shunting-yard_algorithm
# all operators have equal precedence and are left-associative
def shunting_yard(tokens, symbols):
    """
    tokens: [token]
    symbols: {symbol: True|False}
    """
    queue = []
    stack = []
    for token in tokens:
        if token in symbols.keys() + literals.keys():
            queue.append(token)
        elif token in operators.keys() + ['(']:
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                queue.append(stack.pop())
            if not stack: raise UnbalancedParen
            else: stack.pop()
        else: raise InvalidExpression

    if '(' in stack: raise UnbalancedParen
    return queue + list(reversed(stack))

def rpn(tokens, symbols):
    """
    tokens: [token]
    symbols: {symbol: True|False}
    """
    stack = []
    for token in tokens:
        if token in symbols.keys():
            stack.append(symbols[token])
        elif token in literals.keys():
            stack.append(literals[token])
        elif token in operators.keys():
            if num_args[token] > len(stack):
                raise InvalidExpression
            args = [stack.pop() for i in range(num_args[token])]
            stack.append(operators[token](*args))
        else: raise InvalidExpression

    if len(stack) != 1: raise InvalidException
    return stack[0]


########
# Tests 
########
def test(expr, symbols):
    tokens = expr.split()
    tokens = shunting_yard(tokens, symbols)
    result = rpn(tokens, symbols)
    print 'Expression: %s' % expr
    print 'Result: %s ' % result
    print "***********************"

print "***********************"
symbols = {'x': True, 'y': False, 'z': True}
print 'x=true, y=false, z=true'
print "***********************"
test('x', symbols)
test('( not x ) and y', symbols)
test('( ( ( ( x or ( y and z ) ) ) ) ) ', symbols)
test('x and x and x and x and x and x and x and false', symbols)
