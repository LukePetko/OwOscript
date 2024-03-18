class VariableDeclaration:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
    def __str__(self) -> str:
        return f'name: {self.name}, value: {self.value}'

class FunctionDeclaration:
    def __init__(self, name, args, body) -> None:
        self.name = name
        self.args = args
        self.body = body
    def __str__(self) -> str:
        return f'name: {self.name}, args: {self.args}, body: {self.body}'

class ReturnStatement:
    def __init__(self, statement) -> None:
        self.statement = statement
    def __str__(self) -> str:
        return f'statement {self.statement}'

class BinaryOperation:
    def __init__(self, left, right, operation) -> None:
        self.left = left
        self.right = right
        self.operation = operation
    def __str__(self) -> str:
        return f'left: {self.left}, right: {self.right}, operation: {self.operation}'

class NumberLiteral:
    def __init__(self, value) -> None:
        self.value = value
    def __str__(self) -> str:
        return f'value {self.value}'
        
class StringLiteral:
    def __init__(self, value) -> None:
        self.value = value
    def __str__(self) -> str:
        return f'value {self.value}'

class VariableReference:
    def __init__(self, value) -> None:
        self.value = value
    def __str__(self) -> str:
        return f'value {self.value}'

