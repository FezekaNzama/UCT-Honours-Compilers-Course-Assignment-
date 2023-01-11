import ply.yacc as yacc
import lexr
tokens = lexr.tokens

err = False

#viableNames[]

def p_start(p):
    '''start    : assign 
                | end '''
    p[0] = p[1]

def p_assign(p):
    '''assign : NAME '=' expr'''
    #p[0]=('ASSIGN', p[1],p[3])

def p_end(p):
    '''end : END'''
#     p[0] = p[1]
    #print(p[1])
    if(err==True):
        print('Error in input')
    else:
        print("Accepted")
    
def p_expr(p):
    '''expr : expr '+' term
            | expr '+' bracket
            | bracket
            | term '''
#    if (len(p)==4):
#        if p[2] == '+':
#            p[0] = (p[1] + p[2])
#        else:
#            p[0]=p[1]
#    else:
#        p[0]=p[1]

def p_bracket(p):
    '''bracket : '(' expr ')' '''
    global err
    if p[1]=='[': 
        err=True

    if p[3]==']':
        err=True


def p_term(p):
    '''term : NUMBER 
            | NAME '''
#    p[0] = p[1]
            
# Error rule for syntax errors
def p_error(p):
    global err
    err = True
    
    

# Build the parser
parser = yacc.yacc(debug=False, write_tables=False)

readIn =[]

while True:
    line = input()
    if line =='#':
        readIn.append('#END')
        break
    readIn.append(line)

multiline = "\n".join(readIn)

while readIn: 
    parser.parse(readIn.pop(0))

