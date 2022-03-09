from sly import Lexer


class MXLexer(Lexer):

  ignore = r' \t'             # IGNORE TABS AND SPACES
  ignore_comment = r'//.*\n'  # IGNORE COMMENT
  ignore_newline = r'\n+'     # IGNORE NEW LINE

  tokens = {
    # KEYWORDS
    PRINT, LOAD, RANGE, MAX, LINEMAX, COLUMNMAX, IDENT,

    # SYMBOLS = { , | ( | ) }
    LPAREN, RPAREN,

    # OPERATORS = { = , + , - , * , / }
    ASSIGN, PLUS, MINUS, TIMES, DIVIDE,

    # TYPES
    ID, INTEGER, FLOAT, STRING,
  }

  # BEGIN TOKEN REGULAR EXPRESSIONS DEFINITION
  PRINT     = r'PRINT'
  LOAD      = r'LOAD'
  RANGE     = r'RANGE'
  MAX       = r'MAX'
  LINEMAX   = r'LINEMAX'
  COLUMNMAX = r'COLUMNMAX'
  IDENT     = r'IDENT'

  LPAREN    = r'\('
  RPAREN    = r'\)'

  ASSIGN = r'='
  PLUS   = r'\+'
  MINUS  = r'-'
  TIMES  = r'\*'
  DIVIDE = r'/'

  ID = r'[a-zA-Z_]\w*'

  @_(r'\d+\.\d+')
  def FLOAT(self, t):
    t.value = float(t.value)
    return t

  @_(r'\d+')
  def INTEGER(self, t):
    t.value = int(t.value)
    return t

  @_(r'".*"')
  def STRING(self, t):
    t.value = t.value.strip('\"')
    return t
  # END TOKEN REGULAR EXPRESSIONS DEFINITION

  # COUNT LINES IN CODE
  def ignore_newline(self, t):
    self.lineno += t.value.count('\n')

  # ERROR MESSAGE
  def error(self, t):
    print(f'Error: Wrong character "{t.value[0]}" at line: {self.lineno}, column: {self.index + 1}')
    self.index += 1