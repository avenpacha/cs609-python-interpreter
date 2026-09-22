# lexer.py
# lexer owner: LeBrea Franklin
import re

class token:
    def __init__(self, Type, value):
        self.Type = Type
        self.value = value

    def __repr__(self):
        return f"Token(type={self.Type}, value={self.value})"

class Lexer:
    def __init__(self):
        self.keywords = {'let', 'print', 'if', 'else', 'while', 'return'}
        self.token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),
            ('ID',       r'[A-Za-z_]\w*'),
            ('EQUAL',    r'=='),
            ('NEQUAL',   r'!='),
            ('ASSIGN',   r'='),
            ('PLUS',     r'\+'),
            ('MINUS',    r'-'),
            ('MUL',     r'\*'),
            ('DIV',   r'/'),
            ('LESS',     r'<'),
            ('GREATER',  r'>'),
            ('LEFTPAREN',  r'\('),
            ('RIGHTPAREN', r'\)'),
            ('SEMI',     r';'),
            ('SKIP',     r'[ \t\n]+'),
            ('MISMATCH', r'.'),
        ]
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)
        self.get_token = re.compile(self.token_regex).match

    def tokenize(self, code):
        pos = 0
        tokens = []
        while pos < len(code):
            match = self.get_token(code, pos)
            if match is None:
                raise RuntimeError(f'Unexpected character: {code[pos]}')
            lexeme = match.lastgroup
            value = match.group()
            if lexeme == 'NUMBER':
                tokens.append(token('NUMBER', value))
            elif lexeme == 'ID':
                if value in self.keywords:
                    tokens.append(token(value.upper(), value))
                else:
                    tokens.append(token('ID', value))
            elif lexeme in {'ASSIGN', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EQUAL', 'NEQUAL', 'LESS', 'GREATER', 'LEFTPAREN', 'RIGHTPAREN', 'SEMI'}:
                tokens.append(token(lexeme, value))
            elif lexeme == 'SKIP':
                pass
            elif lexeme == 'MISMATCH':
                raise RuntimeError(f'Unexpected character: {value}')
            pos = match.end()
        return tokens
