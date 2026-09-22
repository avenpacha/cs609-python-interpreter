
# main.py
# Integration owner: Veera Venkata Naga Surya Jaya Sai Padala

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def run(source_code):
    """
    Runs a full pipeline: source code -> tokens -> AST -> execution.
    """
    # Step 1: Lexical analysis
    tokens = Lexer().tokenize(source_code)

    # Step 2: Parsing
    ast = Parser(tokens).parse()

    # Step 3: Interpretation
    interpreter = Interpreter()
    interpreter.interpret(ast)


if __name__ == "__main__":
    sample_program = """
    let x = 10 + 5;
    let y = x * 2;
    print(x);
    print(y);
    """

    run(sample_program)
