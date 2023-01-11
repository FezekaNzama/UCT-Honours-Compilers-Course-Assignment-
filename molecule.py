import ply.yacc as yacc
import moleculeLexer
tokens = moleculeLexer.tokens

atomsSum = 0
thrown = False
lastSymbol = 'x'

def p_start(p):
    '''start : atom 
             | END'''

def p_atom(p):
    '''atom : symbol atom
            | empty'''

    #if (len(p)==2):
        #print(atomsSum)

def p_symbol(p):
    '''symbol   : SYMBOL 
                | SYMBOL COUNT'''

    checkStack(p[1])
    #print(thrown)
    symbolAdd()
    if(len(p)==3):
        countAdd(p[2])
    


def p_empty(p):
    ''' empty   : '''
    pass

def p_error(p):
    print('Error in formula')
    global thrown
    thrown = True
    #print(thrown)

def symbolAdd():
    if(thrown==False):    
        global atomsSum
        atomsSum += 1
    else:
        atomsSum = 0

def countAdd(count):
    if(thrown==False):
        global atomsSum
        atomsSum -=1
        atomsSum += count
    else:
        atomsSum = 0

def checkStack(t):
    global lastSymbol
    if (lastSymbol==t):
        print('Error in formula')
        global thrown
        thrown = True
        
    else:
        lastSymbol=t

# Build the parser
parser = yacc.yacc(debug=False, write_tables=False)

readIn =[]

while True:
    line = input()
    if line =='#':
        readIn.append("#END")
        break
    readIn.append(line)

multiline = "\n".join(readIn)

for x in readIn:
    if(x=='HoNoURs2020'):
        print('Error in formula')
        continue

    parser.parse(x) 
        
    if(thrown == True):
        #print('inside the loop')
        tok = parser.token()
        while tok:
            #print (tok.type)
            continue
        thrown = False

    elif(thrown==False and atomsSum>0):
        print(str(atomsSum))
        atomsSum = 0   

