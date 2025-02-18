import re
import jjcli
from collections import Counter

# TODO - frequencias relativas (apareceu 10 vezes em 10 milhoes de palavras p.e.) ... outro ficheiro chamado calculador para somar/subtrair frequências

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def counter(tokens):
    return Counter(*tokens)
    
def main():
    cl = jjcli.clfilter()
    tokens = []
    for txt in cl.text():
        t = lexer(txt)
        print(t)
        tokens.append(t)
    c = counter(tokens)
    print(c)
        
if __name__ == "__main__":
    main()