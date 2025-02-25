import re
import jjcli
from collections import Counter

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def pretty_print(freq, relative_freq, opt):
    #TODO first write the total amount of tokens when dealing with relative frequencies
    if("-a" in opt):
        for word, count in freq.most_common():
            print(f"{count}      {word}")
    else:
        for word, count in relative_freq:
            print(f"{count:.2f}      {word}")

def ratio(relative_freq1, relative_freq2):
    result = {}
    for word, count in relative_freq1:
        result.update({word: count / relative_freq2.get(word, 1/100)})
    pass
    
    

def counter(freq_abs):
    total_tokens = sum(freq_abs.values())
    relative_freq = [(word, count / total_tokens * 1000000) for word, count in freq_abs.most_common()]
    return relative_freq

def main():
    """
    Options:a 
        -a: absolute frequency
        -m 700: top 700 words (FIXME)
        -j: json output (TODO)
        """
    cl = jjcli.clfilter("am:",doc=main.__doc__)
    tokens = []
    for txt in cl.text():
        t = lexer(txt)
        tokens.extend(t)
    c = Counter(tokens)
    relative_frequencies = counter(c)
    pretty_print(c, relative_frequencies, cl.opt)
        
if __name__ == "__main__":
    main()