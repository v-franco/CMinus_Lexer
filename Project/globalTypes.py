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

# StateType
class StateType(Enum):
    START = 0
    INASSIGN = 1
    INCOMMENT = 2
    INNUM = 3
    INID = 4
    DONE = 5

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
    

#***********   Syntax tree for parsing ************

class NodeKind(Enum):
    StmtK = 0
    ExpK = 1

class StmtKind(Enum):
    IfK = 0
    RepeatK = 1
    AssignK = 2
    ReadK = 3
    WriteK = 4

class ExpKind(Enum):
    OpK = 0
    ConstK = 1
    IdK = 2

# ExpType is used for type checking
class ExpType(Enum):
    Void = 0
    Integer = 1
    Boolean = 2

# Máximo número de hijos por nodo (3 para el if)
MAXCHILDREN = 3

class TreeNode:
    def __init__(self):
        # MAXCHILDREN = 3 está en globalTypes
        self.child = [None] * MAXCHILDREN # tipo treeNode
        self.sibling = None               # tipo treeNode
        self.lineno = 0                   # tipo int
        self.nodekind = None              # tipo NodeKind, en globalTypes
        # en realidad los dos siguientes deberían ser uno solo (kind)
        # siendo la  union { StmtKind stmt; ExpKind exp;}
        self.stmt = None                  # tipo StmtKind
        self.exp = None                   # tipo ExpKind
        # en realidad los tres siguientes deberían ser uno solo (attr)
        # siendo la  union { TokenType op; int val; char * name;}
        self.op = None                    # tipo TokenType
        self.val = None                   # tipo int
        self.name = None                  # tipo String
        # for type checking of exps
        self.type = None                  # de tipo ExpType


