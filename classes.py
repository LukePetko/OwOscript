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

class MathOperationDeclaration:
    def __init__(self, left, right, operation) -> None:
        self.left = left
        self.right = right
        self.operation = operation
    def __str__(self) -> str:
        return f'left: {self.left}, right: {self.right}, operation: {self.operation}'
