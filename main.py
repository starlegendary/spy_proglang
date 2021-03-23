from reader import Reader
from lexer import Lexer
import pandas as pd

def run(file_name):
    with open(file_name,'r') as file:
        script = file.read()

    print(script)

    alltoken = Lexer(Reader(script,2)) 
    print(pd.DataFrame(alltoken,columns =  ['type', 'value']))
    
    return 


run('script.spy')
