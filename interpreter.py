
# interpreter.py
# interpreter owner: Veera Venkata Naga Surya Jaya Sai Padala

from ast_nodes import (
    ProgramNode,
    AssignNode,
    PrintNode,
    BinOpNode,
    NumberNode,
    VarNode,
    UnaryOpNode,
)


class Interpreter:
    """
    Walks the AST produced by the Parser and executes it.

    Usage:
        Interpreter().interpret(ast)
    """

    def __init__(self):
        # Stores variable name -> value bindings created by AssignNode statements.
        self.variables = {}

    def interpret(self, ast):
        """Entry point. Executes a ProgramNode (the root of the AST)."""
        return self.visit(ast)

    # Dispatch

    def visit(self, node):
        """
        Routes each node to its matching visit_<NodeType> method.
        Example: a BinOpNode is routed to visit_BinOpNode.
        """
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    # Program / statements

    def visit_ProgramNode(self, node: ProgramNode):
        for statement in node.statements:
            self.visit(statement)

    def visit_AssignNode(self, node: AssignNode):
        value = self.visit(node.expr)
        self.variables[node.var_name] = value

    def visit_PrintNode(self, node: PrintNode):
        value = self.visit(node.expr)
        print(value)

    # Expressions

    def visit_BinOpNode(self, node: BinOpNode):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op == "PLUS":
            result = left + right
        elif node.op == "MINUS":
            result = left - right
        elif node.op == "MUL":
            result = left * right
        elif node.op == "DIV":
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            result = left / right
            # Keep whole-number results as ints (e.g. 10 / 2 -> 5, not 5.0)
            if isinstance(left, int) and isinstance(right, int) and result.is_integer():
                result = int(result)
        else:
            raise Exception(f"Unknown operator: {node.op}")

        return result

    def visit_UnaryOpNode(self, node: UnaryOpNode):
        value = self.visit(node.expr)
        if node.op == "MINUS":
            return -value
        elif node.op == "PLUS":
            return value
        else:
            raise Exception(f"Unknown unary operator: {node.op}")

    def visit_NumberNode(self, node: NumberNode):
        return node.value

    def visit_VarNode(self, node: VarNode):
        if node.name not in self.variables:
            raise Exception(f"Undefined variable: {node.name}")
        return self.variables[node.name]
