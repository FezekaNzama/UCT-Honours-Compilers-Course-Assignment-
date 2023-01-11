import ply.lex as lex

tokens = [
    'END',
    'SYMBOL',
    'COUNT'
]

t_ignore  = ' \t'
t_END = r'\#END'
t_SYMBOL = r'A[lrsgtucm]?|B[aerikh]?|C[alroufsemfnd]?|D[bsy]|E[urs]|F[erml]?|G[aed]|H[efgos]?|I[nr]?|L[auirv]|M[dgnoct]|N[abdeipoh]?|O[sg]?|P[rmdbotau]?|R[buhgfena]|S[ciernbmg]?|T[icebhmals]|Z[nr]|Kr?|Xe|Yb?|W|U|V'

def t_COUNT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_error(t):
    #print("Illegal Character " + "\'" + t.value[0] + "\'")
    t.lexer.skip(1)

lexer = lex.lex()

#data = "C169719H270466N45688O52238S911#"

#lex.input(data)

#while True: 
#    tok = lexer.token()
#    if tok.type == 'END':
#        break
#    elif tok.type == 'COUNT':
#        print("\'"+ tok.type + "\' "+ str(tok.value))
#    else:
#        print("\'"+ tok.type + "\' \'" + tok.value + "\'")

