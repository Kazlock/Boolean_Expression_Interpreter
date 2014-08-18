from bei_functions import *
from bei_exceptions import *

keywords = ['true', 'false', 'and', 'or', 'not', '(', ')']

literals   = {'true': True, 'false': False}
binary_ops = {'and': bei_and, 'or': bei_or}
unary_ops  = {'not': bei_not}
operators  = binary_ops.keys() + unary_ops.keys()

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
        if token in operators + ['(']:
            stack.append(token)
        if token == ')':
            while stack and stack[-1] != '(':
                queue.append(stack.pop())
            if not stack: raise UnbalancedParen
            else: stack.pop()
    if '(' in stack: raise UnbalancedParen
    return queue + list(reversed(stack))

expr = "( not x ) or true"
tokens = expr.split()
print expr
print shunting_yard(tokens, {'x': True})
