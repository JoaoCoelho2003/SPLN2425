import re
import jjcli
from collections import Counter

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def counter(tokens):
    total_tokens = sum(tokens.values())
    relative_freq = {word: (count, count / total_tokens) for word, count in tokens.items()}
    return relative_freq

def main():
    cl = jjcli.clfilter()
    tokens = []
    for txt in cl.text():
        t = lexer(txt)
        print(t)
        tokens.extend(t)
    c = Counter(tokens)
    relative_frequencies = counter(c)
    print(relative_frequencies)
        
if __name__ == "__main__":
    main()