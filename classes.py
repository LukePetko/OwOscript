import json 

class AST:
    def __init__(self, body) -> None:
        self.body = body
    def to_dict(self):
        body_dicts = [item.to_dict() if hasattr(item, 'to_dict') else item for item in self.body]
        return {
            'type': 'AST',
            'body': body_dicts
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class VariableDeclaration:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
    def to_dict(self):
        json_dict = {
            'type': 'VariableDeclaration',
            'name': self.name,
            'value': self.value.to_dict() if hasattr(self.value, 'to_dict') else self.value
        }
        return json_dict
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class FunctionDeclaration:
    def __init__(self, name, args, body) -> None:
        self.name = name
        self.args = args
        self.body = body
    def to_dict(self):
        body_dicts = [item.to_dict() if hasattr(item, 'to_dict') else item for item in self.body]
        args_dicts = [item.to_dict() if hasattr(item, 'to_dict') else item for item in self.args]
        return {
            'type': 'FunctionDeclaration',
            'name': self.name.to_dict() if hasattr(self.name, 'to_dict') else self.name,
            'args': args_dicts,
            'body': body_dicts
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class ReturnStatement:
    def __init__(self, statement) -> None:
        self.statement = statement
    def to_dict(self):
        return {
            'type': 'ReturnStatement',
            'statement': self.statement.to_dict() if hasattr(self.statement, 'to_dict') else self.statement
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class BinaryOperation:
    def __init__(self, left, right, operation) -> None:
        self.left = left
        self.right = right
        self.operation = operation
    def to_dict(self):
        return {
            'type': 'BinaryOperation',
            'left': self.left.to_dict() if hasattr(self.left, 'to_dict') else self.left,
            'right': self.right.to_dict() if hasattr(self.right, 'to_dict') else self.right,
            'operation': self.operation.to_dict() if hasattr(self.operation, 'to_dict') else self.operation
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class FunctionExecution:
    def __init__(self, name, args) -> None:
        self.name = name
        self.args = args
    def to_dict(self):
        args_dicts = [item.to_dict() if hasattr(item, 'to_dict') else item for item in self.args]
        return {
            'type': 'FunctionExecution',
            'name': self.name.to_dict() if hasattr(self.name, 'to_dict') else self.name,
            'args': args_dicts
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())
        

class NumberLiteral:
    def __init__(self, value) -> None:
        self.value = value
    def to_dict(self):
        return {
            'type': 'NumberLiteral',
            'value': self.value.to_dict() if hasattr(self.value, 'to_dict') else self.value
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())
        
class StringLiteral:
    def __init__(self, value) -> None:
        self.value = value
    def to_dict(self):
        return {
            'type': 'StringLiteral',
            'value': self.value.to_dict() if hasattr(self.value, 'to_dict') else self.value
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class VariableReference:
    def __init__(self, value) -> None:
        self.value = value.to_dict() if hasattr(value, 'to_dict') else value
    def to_dict(self):
        return {
            'type': 'VariableReference',
            'value': self.value
        }
    def __str__(self) -> str:
        return json.dumps(self.to_dict())

