from sly import Parser
from lang.MXLexer import MXLexer

import numpy as np

class MXParser(Parser):

  tokens = MXLexer.tokens

  precedence = (
    ('left' ,PRINT  ,),                          # FUNCTIONS
    ('left' ,LOAD  ,),                           # FUNCTIONS
    ('left' ,PLUS  ,MINUS ,),                    # OPERATIONS
    ('left' ,TIMES ,DIVIDE,),                    # HIGH PRIORITY OPERATIONS
    ('right',UMINUS,),                           # UNARY OPERATORS
  )

  def __init__(self):
    self.ids = {}

  @_('PRINT expr')
  def statement(self, p):
    return print(p.expr)

  @_('ID ASSIGN expr')
  def statement(self, p):
    self.ids[p.ID] = p.expr

  @_('expr')
  def statement(self, p):
    pass

  @_('expr PLUS expr')
  def expr(self, p):
    return p.expr0 + p.expr1

  @_('expr MINUS expr')
  def expr(self, p):
    return p.expr0 - p.expr1

  @_('expr TIMES expr')
  def expr(self, p):
    return p.expr0 * p.expr1

  @_('expr DIVIDE expr')
  def expr(self, p):
    return p.expr0 / p.expr1

  @_('MINUS expr %prec UMINUS')
  def expr(self, p):
    return -p.expr

  @_('LPAREN expr RPAREN')
  def expr(self, p):
    return p.expr

  @_('FLOAT')
  def expr(self, p):
    return float(p.FLOAT)

  @_('INTEGER')
  def expr(self, p):
    return int(p.INTEGER)

  @_('STRING')
  def expr(self, p):
    return str(p.STRING)

  @_('ID')
  def expr(self, p):
    try:
      return self.ids[p.ID]
    except LookupError:
      print(f'Undefined name {p.ID!r}')

  @_('LOAD STRING')
  def expr(self, p):
    return np.array(eval(p.STRING))
