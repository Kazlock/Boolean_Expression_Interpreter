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
        elif token in operators + ['(']:
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                queue.append(stack.pop())
            if not stack: raise UnbalancedParen
            else: stack.pop()
        else: raise InvalidExpression()

    if '(' in stack: raise UnbalancedParen
    return queue + list(reversed(stack))

expr = "( not x ) or true"
tokens = expr.split()
print expr
print shunting_yard(tokens, {'x': True})
