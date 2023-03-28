import ply.lex as lex

# Define the tokens that our lexer will recognize
tokens = (
    'TYPE',
    'COMMENT',
    'FOR_LOOP',
    'IN',
    'IF',
    'ELSE',
    'FUNCTION',
    'PROGRAM',
    'ID',
    'NUMBER',
    'COMMENT_OPEN',
    'COMMENT_CLOSE',
    'TEXT',
    'RANGE'
)

# erals are characters or strings that represent themselves as tokens
literals = (',',',','=','(',')','{','}','<','>','[',']',r'+',r'-','/',r'*')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
#t_STOP = r'STOP'
t_ASSIGN = r'[a-zA-Z]+' # POR O STOP AQUI??
t_N = r'\n'

operacoes="+-/*="

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ANY_ignore = ' \t\n'


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()






while(True):
    i = input(">")
    lexer.input(i)
    for tok in lexer:
        if(tok.value == 'STOP') : quit()
        if(tok.type == 'ASSIGN') : print("variavel " + tok.value)
        if(str(tok.value) in operacoes) : print('operador encontrado')
        if(tok.type == 'N'):print()
        print(tok)

