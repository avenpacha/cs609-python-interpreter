
# Building a Custom Interpreter in Python

**CS609 — Advanced Programming Languages | Team Project**

This project implements a small custom-language interpreter in Python. It
processes source code through lexical analysis, parsing, and interpretation.

The supported language includes variable assignments, arithmetic expressions,
print statements, and multiple statements.

## How It Works

1. `lexer.py` breaks source code into tokens.
2. `parser.py` uses the tokens to construct an Abstract Syntax Tree (AST).
3. `ast_nodes.py` defines the structures used to represent instructions.
4. `interpreter.py` evaluates the AST and executes the instructions.
5. `main.py` connects the components.

## Example

```text
let x = 10 + 5;
let y = x * 2;
print(x);
print(y);
```

Expected output:

```text
15
30
```

## My Contribution

**Aven Pacha Pinto — AST Nodes and Parser**

I developed `ast_nodes.py` and `parser.py`, which organize the tokenized
instructions into a structure the interpreter can evaluate.

All group members contributed to testing, documentation, and demonstration.

## Potential Real-World Application

The language-processing concepts used in this project could support
applications that evaluate limited, predefined rules.

For example, an academic advising application could use a custom rules
interpreter to process course requirements or credit-hour calculations.
A production system would require additional functionality and safeguards
beyond those implemented in this course project.

## Project Report

[Read the project report](docs/CS609_Interpreter_Project_Report_Redacted.pdf)

## Project Scope

This is a course project implementing a limited custom language in Python.
It is not a complete Python interpreter or a production-ready academic
advising system.
