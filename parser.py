import re
from reader import Reader

def Parser(alltoken):
    tree = {}
    ttt = Reader(alltoken)
    

    def inner(prev):
        return

def futuexp(prev,ttt):
    curr, futu = ttt.curr, ttt.futu

    if(curr[0] in ('num','str','given','func')):
        return




