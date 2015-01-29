class UnbalancedParen(Exception):
    def __str__(self):
        return "Parenthesis are unbalanced"

class InvalidExpression(Exception):
    pass

class UndefinedToken(Exception):
    def __init__(self, token):
        self.token = token

    def __str__(self):
        return "Undefined token '" + self.token + "'"
