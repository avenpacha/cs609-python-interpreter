
# parser.py
# Parser/AST owner: Aven Pacha

from ast_nodes import (
    ProgramNode,
    AssignNode,
    PrintNode,
    BinOpNode,
    NumberNode,
    VarNode,
    UnaryOpNode
)


class Parser:
    def __init__(self, tokens):
        # Store the tokens created by the lexer
        self.tokens = tokens

        # Keep track of the current token
        self.position = 0


    def current_token(self):
        """Return the current token or None if there are no tokens left."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]

        return None


    def consume(self, expected_type):
        """
        Check that the current token is the expected type,
        then move to the next token.
        """
        current = self.current_token()

        if current is None:
            raise SyntaxError(
                f"Expected {expected_type}, but reached the end of the program."
            )

        if current.Type != expected_type:
            raise SyntaxError(
                f"Expected {expected_type}, but found {current.Type}."
            )

        self.position += 1
        return current


    def parse(self):
        """
        Parse all statements and place them inside a ProgramNode.
        """
        statements = []

        while self.current_token() is not None:
            statement = self.parse_statement()
            statements.append(statement)

        return ProgramNode(statements)


    def parse_statement(self):
        """
        Decide whether the next statement is an assignment
        or a print statement.
        """
        current = self.current_token()

        if current.Type == "LET":
            return self.parse_assignment()

        if current.Type == "PRINT":
            return self.parse_print()

        raise SyntaxError(
            f"Expected LET or PRINT, but found {current.Type}."
        )


    def parse_assignment(self):
        """
        Parse an assignment such as:

            let x = 10 + 5;
        """
        self.consume("LET")

        variable_token = self.consume("ID")
        variable_name = variable_token.value

        self.consume("ASSIGN")

        expression = self.parse_expression()

        self.consume("SEMI")

        return AssignNode(variable_name, expression)


    def parse_print(self):
        """
        Parse a print statement such as:

            print(x);
        """
        self.consume("PRINT")
        self.consume("LEFTPAREN")

        expression = self.parse_expression()

        self.consume("RIGHTPAREN")
        self.consume("SEMI")

        return PrintNode(expression)


    def parse_expression(self):
        """
        Parse addition and subtraction.

        Example:
            10 + 5
        """
        node = self.parse_term()

        while (
            self.current_token() is not None
            and self.current_token().Type in ("PLUS", "MINUS")
        ):
            operator = self.current_token().Type
            self.consume(operator)

            right_side = self.parse_term()
            node = BinOpNode(node, operator, right_side)

        return node


    def parse_term(self):
        """
        Parse multiplication and division.

        This method gives multiplication and division
        higher priority than addition and subtraction.
        """
        node = self.parse_factor()

        while (
            self.current_token() is not None
            and self.current_token().Type in ("MUL", "DIV")
        ):
            operator = self.current_token().Type
            self.consume(operator)

            right_side = self.parse_factor()
            node = BinOpNode(node, operator, right_side)

        return node


    def parse_factor(self):
        """
        Parse a single number, variable, parenthesized expression,
        or unary operation.

        Examples:
            10
            x
            (10 + 5)
            -5
            -x
        """
        current = self.current_token()

        if current is None:
            raise SyntaxError("Expected a number, variable, or expression.")

        # Unary minus or unary plus
        # Example: -5 becomes UnaryOpNode("MINUS", NumberNode(5))
        if current.Type in ("MINUS", "PLUS"):
            operator = current.Type
            self.consume(operator)
            expression = self.parse_factor()
            return UnaryOpNode(operator, expression)

        if current.Type == "NUMBER":
            number_token = self.consume("NUMBER")

            # Convert numbers with decimals to float
            if "." in str(number_token.value):
                value = float(number_token.value)
            else:
                value = int(number_token.value)

            return NumberNode(value)

        if current.Type == "ID":
            variable_token = self.consume("ID")
            return VarNode(variable_token.value)

        if current.Type == "LEFTPAREN":
            self.consume("LEFTPAREN")
            expression = self.parse_expression()
            self.consume("RIGHTPAREN")
            return expression

        raise SyntaxError(
            f"Expected a number, variable, parenthesized expression, or unary operator, "
            f"but found {current.Type}."
        )
