import ply.lex as lex

tokens = [
    'NUMBER',
    'NAME',
    'END'
]

t_ignore  = ' \t'
t_NAME =  r'[a-zA-Z_][a-zA-Z0-9_]*'
t_END = r'\#END'
literals = ['+','=','(',')','[',']']

def LSquare(t):
    r'\['
    t.type = '['
    return t_error(t)

def RSquare(t):
    r'\]'
    t.type = ']'
    return t_error(t)

def LParen(t):
    r'\('
    t.type = '('
    return t

def RParen(t):
    r'\)'
    t.type = '('
    return t

def Plus(t):
    r'\+'
    t.type = '+'
    return t

def Equals(t):
    r'='
    t.type = '='
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(input, t):
    line_start = input.rfind('\n', 0, t.lexpos)+1
    return(t.lexpos - line_start)

def t_error(t):
    #print("Illegal character " + "\'" + t.value[0] + "\'")
    t.lexer.skip(1)

lexer = lex.lex()



