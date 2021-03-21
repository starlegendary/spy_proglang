from lexer import Lexer
from reader import Reader
import pandas as pd
def run(file_name):
  with open(file_name,'r') as file:
      script = file.read().replace('\n', '')
  return Lexer(script)

print(pd.DataFrame(run('script.spy'),columns =  ['type', 'value']))