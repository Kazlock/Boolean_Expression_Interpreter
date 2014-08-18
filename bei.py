from bei_functions import *
from bei_exceptions import *
from itertools import *

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

# http://en.wikipedia.org/wiki/Reverse_Polish_notation
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

def evaluate(expr, symbols):
    tokens = expr.split()
    tokens = shunting_yard(tokens, symbols)
    return rpn(tokens, symbols)

def gen_truth_table(expr):
    """
    expr: str
    symbols: [str]
    """
    symbols = set(filter(lambda x: x not in keywords, expr.split()))
    header = ''
    for s in symbols: header += '  %s  |' % s
    line_break = ''.join(['-' for i in range(len(header)+len(expr)+1)])
    print header + ' ' + expr
    print line_break
    permutations = list(product((True, False), repeat=len(symbols)))
    for p in permutations:
        p_symbols = {}
        line = ''
        for i, s in enumerate(symbols):
            line += str(p[i])
            if p[i] == True: line += ' '
            line += str('|')
            p_symbols[s] = p[i]
        print line + ' ' + str(evaluate(expr, p_symbols))
        print line_break


gen_truth_table('x and ( y or not z )')
