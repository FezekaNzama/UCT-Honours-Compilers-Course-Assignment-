import ply.lex as lex

tokens =[
    'END',
    'NEWLINE'
    'NUMBER',
    'NAME',
    
]

t_NEWLINE = r'\n'
t_ignore  = ' \t'
t_NAME =  r'[a-zA-Z_][a-zA-Z0-9_]*'
t_END = r'\#END'
literals = ['+','=','(',')']

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
    print("Illegal character " + "\'" + t.value[0] + "\'")
    t.lexer.skip(1)

lexer = lex.lex()

readIn =[]

while True:
    line = input()
    if line =='#':
        readIn.append('#END')
        break
    readIn.append(line)

multiline = "\n".join(readIn)

lex.input(multiline)

while True:
    tok = lexer.token()
    if tok.type=='END':
        break
    if tok.type =='NUMBER':
        print("(\'" + tok.type +"\'"+", "+ str(tok.value) +", " + str(tok.lineno) + ", "+ str(tok.lexpos) +")")
    else:
        print("(\'" + tok.type +"\'"+", "+"\'"+ str(tok.value) +"\'" +", " + str(tok.lineno) + ", "+ str(tok.lexpos) +")")
