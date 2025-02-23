import sys
import re
from collections import Counter

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def counter(tokens):
    total_tokens = sum(tokens.values())
    return {word: (count, count / total_tokens) for word, count in tokens.items()} if total_tokens > 0 else {}

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"add", "sub"}:
        print("Usage: ftk-freq <add|sub>")
        sys.exit(1)

    operation = sys.argv[1]
    combined_freq = Counter()

    try:
        for line in sys.stdin:
            tokens = lexer(line)
            token_counts = Counter(tokens)

            if operation == "add":
                combined_freq += token_counts
            elif operation == "sub":
                combined_freq -= token_counts

    except KeyboardInterrupt:
        pass

    combined_freq = Counter({word: max(0, count) for word, count in combined_freq.items()})

    relative_frequencies = counter(combined_freq)
    print(relative_frequencies)

if __name__ == "__main__":
    main()