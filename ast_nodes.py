
# ast_nodes.py
# Parser/AST owner: Aven Pacha

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union


# Base node types

class ASTNode:
    """Base class for all AST nodes."""
    pass


class StatementNode(ASTNode):
    """Base class for statement nodes."""
    pass


class ExpressionNode(ASTNode):
    """Base class for expression nodes."""
    pass


# Program

@dataclass
class ProgramNode(ASTNode):
    """Root node. Holds all statements in the program in execution order."""
    statements: List[StatementNode]


# Statements

@dataclass
class AssignNode(StatementNode):
    """
    Represents a variable assignment.

    Example source:
        let x = 10 + 5;

    AST shape:
        AssignNode(var_name="x", expr=BinOpNode(...))
    """
    var_name: str
    expr: ExpressionNode


@dataclass
class PrintNode(StatementNode):
    """
    Represents a print statement.

    Example source:
        print(x);
    """
    expr: ExpressionNode


# Expressions

@dataclass
class BinOpNode(ExpressionNode):
    """
    Represents a binary arithmetic operation.

    Examples:
        10 + 5
        x * 2
    """
    left: ExpressionNode
    op: str
    right: ExpressionNode


@dataclass
class NumberNode(ExpressionNode):
    """Represents a numeric literal."""
    value: Union[int, float]


@dataclass
class VarNode(ExpressionNode):
    """Represents use of a variable by name."""
    name: str


@dataclass
class UnaryOpNode(ExpressionNode):
    """
    Represents a unary operation, mainly useful for negative numbers.

    Example:
        -5
    """
    op: str
    expr: ExpressionNode
