from enum import Enum

# TokenType
class TokenType(Enum):
    ENDFILE = 300
    ERROR = 301
    # reserved words
    IF = 'if'
    ELSE = 'else'
    INT = 'int'
    RETURN = 'return'
    VOID = 'void'
    WHILE = 'while'
    INPUT = 'input'
    OUTPUT = 'output'
    # multicharacter tokens
    ID = 310
    NUM = 311
    # special symbols
    EQUAL_TO = '=='
    ASSIGN = '='
    NOT_EQUAL_TO = '!='
    LESS_THAN = '<'
    LESS_OR_EQUAL_TO = '<='
    MORE_THAN = '>'
    MORE_OR_EQUAL_TO = '>='
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    SLASH = '/'
    LPAREN = '('
    RPAREN = ')'
    LBRACKET = '['
    RBRACKET = ']'
    LCURLY = '{'
    RCURLY = '}'
    SEMI = ';'
    COMMENT = '/*'
    COMMA = ','
    CLOSE_COMMENT = '*/'

# ReservedWords
class ReservedWords(Enum):
    IF = 'if'
    ELSE = 'else'
    INT = 'int'
    RETURN = 'return'
    VOID = 'void'
    WHILE = 'while'
    INPUT = 'input'
    OUTPUT = 'output'