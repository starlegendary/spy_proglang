import re
from reader import Reader
def Lexer(script):
    alltoken = []
    r = Reader(script)
    def totoken(curr, futu):
        if(curr in " /n"): pass
        else: 
            alltoken.append(token(curr,r))
        if(r.futu != None): 
            r.tofutu()
            return totoken(r.curr, r.futu)
        else: 
            return alltoken
    return totoken(r.curr, r.futu)
def token(curr,r):
      v = str(curr)
      if   curr in "({":     t = 'lll'
      elif curr in ")}":     t = 'rrr'
      elif curr in "+-*/%,:=": t = 'op'
      elif curr in ";":      t = 'end'
      #elif re.match(r'//.*', curr): #add comment
      #    t,v = 'com', find(r,r'//.*','com')
      elif re.match("[_a-zA-Z]", curr):
          t,v = "func",find(r, "\w", 'func')

      elif curr in ("'", '"'): 
          t,v = 'str',find(r, "\w", 'str')

      elif re.match(r'^\d*[.]?\d*$', curr): 
          t,v = "num",find(r, r'^\d*[.]?\d*$','num')
      return (t,v)
def find(r, allowed, type_):
    if(type_ == 'str'): r.tofutu()
    result, futu =  r.curr, r.futu
    while futu is not None and re.match(allowed, futu):
        curr, futu = r.tofutu()
        result += curr
    if(type_ == 'str'): r.tofutu()
    return result