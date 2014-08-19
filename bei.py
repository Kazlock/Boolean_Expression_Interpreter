from bei_functions import *
from bei_exceptions import *
from util import *
from itertools import *

keywords = ['true', 'false', 'and', 'or', 'not', '(', ')']

literals  = {'true': True, 'false': False}
operators = {'and': bei_and, 'or': bei_or, 'not': bei_not}
num_args  = {'and': 2, 'or': 2, 'not': 1}

# en.wikipedia.org/wiki/Shunting-yard_algorithm
# all operators have equal precedence and are left-associative
def shunting_yard(tokens, symbols): # -> [str]
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
def rpn(tokens, symbols): # -> Boolean
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

def evaluate(expr, symbols): # -> Boolean
    """
    expr: str
    symbols: {symbol: True|False}
    """
    tokens = expr.split()
    tokens = shunting_yard(tokens, symbols)
    return rpn(tokens, symbols)

def get_unique_symbols(expr): # -> [str]
    """
    expr: str
    """
    symbols = filter(lambda x: x not in keywords, expr.split())
    del_duplicates(symbols)
    return symbols

def create_truth_table(expr): # -> [[(s1,T|F), (s2,T|F)... expr_result]... ] 
    """
    expr: str
    """
    symbols      = get_unique_symbols(expr)
    permutations = list(product((True, False), repeat=len(symbols))) 
    truth_table  = []
    for p in permutations:
        row = []
        symbol_vals = {}
        for i, s in enumerate(symbols):
            row.append((s,p[i]))
            symbol_vals[s] = p[i]
        row.append(evaluate(expr, symbol_vals))
        truth_table.append(row)
    return truth_table

def sort_truth_table(tt): # -> None
    """
    tt: see create_truth_table()
    """
    for i, row in enumerate(tt):
        tt[i][0:len(row)-1] = sorted(tt[i][0:len(row)-1], key=lambda s: s[0])

def compare_exprs(expr1, expr2): # -> Boolean
    """
    expr1: str
    expr2: str
    """
    tt1 = create_truth_table(expr1)
    tt2 = create_truth_table(expr2)
    sort_truth_table(tt1)
    sort_truth_table(tt2)
    for row in tt1:
        if row not in tt2:
            return False
    return True

print compare_exprs('( x and y ) or ( x and z )', 'x and ( y or z )')
