# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")

import random

import ply.ctokens

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'DICE','NAME','NUMBER','FLOAT',
    )

literals = ['=','+','-','*','/', '(',')', ',',]

# Tokens

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_DICE(t):
    r'![0-9]+[dD][0-9]+'
    t.value = map(int, t.value[1:].upper().split('D'))
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = long(t.value)
    return t

def t_FLOAT(t):
    t.value = float(t.value)
    return t
t_FLOAT.__doc__ = ply.ctokens.t_FLOAT

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_dice(p):
    "expression : DICE"
    count, faces = p[1]
    p[0] = sum(map(lambda p: random.randint(1, faces), xrange(count)))

def p_expression_number(p):
    """expression : NUMBER
                  | FLOAT"""
    p[0] = p[1]

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def setup_readline():
    import atexit, os

    # Setup history
    histfile = 'calc.hist'
    os.system('touch %s' % histfile)
    readline.read_history_file(histfile)
    atexit.register(readline.write_history_file, histfile)

try:
    import readline
    setup_readline()

except ImportError:
    print 'Cannot import readline'

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
